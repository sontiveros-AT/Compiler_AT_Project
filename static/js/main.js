// @main.js Copyright (c) 2020 Jalasoft.
// 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
// 1376 subsuelo Edif. La Unión, Av. Gral. Inofuentes, Calacoto, La Paz, Bolivia
// All rights reserved.
//
// This software is the confidential and proprietary information of
// Jalasoft, ("Confidential Information"). You shall not
// disclose such Confidential Information and shall use it only in
// accordance with the termns of the license agreement you entered into
// with Jalasoft.
//
// Author: Andres Cox
// Version: 1.0

// Ip Dom Origin
ip = "192.168.33.10";
port = "8000";

// get current project id
url = window.location.href.split("/");
project_id = url[url.length - 1];

// nodes and editor state
var programDisplayed = "";
var activeNode;

// ztree Settings
var setting = {
    view: {
        addHoverDom: addHoverDom,
        removeHoverDom: removeHoverDom,
        selectedMulti: false,
    },
    check: {
        enable: false,
    },
    data: {
        simpleData: {
            enable: true,
        },
    },
    edit: {
        enable: true,
        showRemoveBtn: showRemoveBtn,
        showRenameBtn: false,
    },
    callback: {
        onClick: onClick,
        onRemove: onRemove,
        onRename: onRename,
    },
};

// Hover UI methods
function addHoverDom(treeId, treeNode) {
    var sObj = $("#" + treeNode.tId + "_span");
    if (treeNode.isParent) {
        if (treeNode.editNameFlag || $("#addFileBtn_" + treeNode.tId).length > 0)
            return;
        if (treeNode.editNameFlag || $("#addDirBtn_" + treeNode.tId).length > 0)
            return;
        var addFileStr =
            "<span class='button add' id='addFileBtn_" +
            treeNode.tId +
            "' title='add file' onfocus='this.blur();'></span>";
        var addDirStr =
            "<span class='button folder' id='addDirBtn_" +
            treeNode.tId +
            "' title='add folder' onfocus='this.blur();'></span>";
        sObj.after(addDirStr);
        sObj.after(addFileStr);
        var btnFile = $("#addFileBtn_" + treeNode.tId);
        var btnDir = $("#addDirBtn_" + treeNode.tId);
        if (btnFile)
            btnFile.bind("click", function () {
                var zTree = $.fn.zTree.getZTreeObj("treeDemo");
                zTree.addNodes(treeNode, { name: `` });
                zTree.editName(treeNode.children[treeNode.children.length - 1]);
                return false;
            });
        if (btnDir)
            btnDir.bind("click", function () {
                var zTree = $.fn.zTree.getZTreeObj("treeDemo");
                zTree.addNodes(treeNode, { name: ``, isParent: true });
                zTree.editName(treeNode.children[treeNode.children.length - 1]);
                return false;
            });
    }
}

function removeHoverDom(treeId, treeNode) {
    $("#addFileBtn_" + treeNode.tId)
        .unbind()
        .remove();
    $("#addDirBtn_" + treeNode.tId)
        .unbind()
        .remove();
}

function showRemoveBtn(treeId, treeNode) {
    var mainFiles = ["main", "main.py", "main.java", "main.js", "main.php"];
    if (!mainFiles.includes(treeNode.name.toLowerCase()) && !treeNode.isParent) {
        return treeNode.name;
    }
}

//Button Methods
function onRemove(e, treeId, treeNode) {
    RemoveFile(treeNode.fileId);
}

function onRename(e, treeId, treeNode) {
    var zTree = $.fn.zTree.getZTreeObj("treeDemo");
    var mainFiles = ["main", "main.py", "main.java", "main.js", "main.php"];
    if (!treeNode.isParent) {
        if (treeNode.name.length == 0) {
            alert("file name can not be empty.");
            zTree.removeNode(treeNode);
        } else if (mainFiles.includes(treeNode.name.toLowerCase())) {
            alert("file name can not be 'main'");
            zTree.removeNode(treeNode);
        } else {
            AddFile(treeNode);
        }
    }
}

function onClick(e, treeId, treeNode) {
    if (activeNode !== undefined) {
        onSave();
    }
    editor.setValue(treeNode.program);
    programDisplayed = treeNode.program;
    activeNode = treeNode;
}

function onSave(treeNode) {
    var program = editor.getValue();
    SaveFile(activeNode.fileId, program);
    if (program !== "") {
        activeNode.program = program;
    }
}

// Cookie Method
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// REST queries
function RunCode() {
    var program = editor.getValue();
    activeNode.program = program;
    file_id = activeNode.fileId;
    SaveFile(file_id, program);
    fetch(`http://${ip}:${port}/api/v1/project/${project_id}/run`, {
        method: "GET",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "X-Requested-With": "XMLHttpRequest",
        },
    })
        .then((res) => res.json())
        .then((data) => {
            document.getElementById("output").innerHTML = data.output;
        });
}

function AddFile(treeNode) {
    var form = new FormData();
    var path = "";
    var pathArray = [];
    parentNode = treeNode.getParentNode();

    while (parentNode.level !== 0) {
        pathArray.push(parentNode.name);
        parentNode = parentNode.getParentNode();
    }

    fileName = treeNode.name;
    path = pathArray.reverse().join("/");
    form.append("fileName", fileName);
    form.append("filePath", path);
    fetch(`http://${ip}:${port}/api/v1/project/${project_id}`, {
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "X-Requested-With": "XMLHttpRequest",
        },
    }).then((res) => {
        fetch(`http://${ip}:${port}/api/v1/project/json/${project_id}`)
            .then((res) => res.json())
            .then((data) => {
                editor.session.setMode(`ace/mode/${data.languageName}`);
                var zNodes = data.content;
                $(document).ready(function () {
                    $.fn.zTree.init($("#treeDemo"), setting, zNodes);
                });
                var zTree = $.fn.zTree.getZTreeObj("treeDemo");
                lastNodeAdded = zTree.getNodeByParam("name", fileName, null);
                LoadFile(lastNodeAdded);
            });
    });
}

function LoadFile(treeNode) {
    var zTree = $.fn.zTree.getZTreeObj("treeDemo");
    zTree.selectNode(treeNode);
    if (activeNode !== undefined) {
        onSave();
    }
    editor.setValue(treeNode.program);
    programDisplayed = treeNode.program;
    activeNode = treeNode;
}

function SaveFile(file_id, program) {
    var form = new FormData();
    form.append("_method", "put");
    form.append("program", program);
    fetch(`http://${ip}:${port}/api/v1/file/${file_id}`, {
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "X-Requested-With": "XMLHttpRequest",
        },
    })
        .then((res) => res.json())
        .then((data) => { });
}

function RemoveFile(fileIdd) {
    var form = new FormData();
    var fileId = fileIdd;
    form.append("_method", "delete");
    fetch(`http://${ip}:${port}/api/v1/file/${fileId}`, {
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "X-Requested-With": "XMLHttpRequest",
        },
    });
}

function DeleteProject(projectIdd) {
    var projectId = projectIdd;
    fetch(`http://${ip}:${port}/api/v1/project/${projectId}`, {
        method: "DELETE",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "X-Requested-With": "XMLHttpRequest",
        },
    }).then(location.reload());
}
