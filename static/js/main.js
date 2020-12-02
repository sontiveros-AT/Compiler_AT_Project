// get current project id
url = window.location.href;
project_id = url.substr(url.length - 1);

// nodes and editor state
var programDisplayed = "";
var activeNode;

// ztree Settings
var setting = {
    view: {
        addHoverDom: addHoverDom,
        removeHoverDom: removeHoverDom,
        selectedMulti: false
    },
    check: {
        enable: false
    },
    data: {
        simpleData: {
            enable: true
        }
    },
    edit: {
        enable: true,
        showRemoveBtn: showRemoveBtn,
        showRenameBtn: false
    },
    callback: {
        onClick: onClick,
        onRemove: onRemove,
        onRename: onRename
    }
};

// zTree nodes
var zNodes =[
    { name: `pydemo7`, open:true, isParent: true,
        children: [
            { name: `main`, fileId: `39`, program: `print("hello world")`},
            { name: `newFile11`, fileId: `53`, program: `print("hello world file 11")`},
            { name: `newFile12`, fileId: `54`, program: `print("hello world file 12")`}
        ]
    }
];

//zTree initialize
$(document).ready(function(){
    $.fn.zTree.init($("#treeDemo"), setting, zNodes);
});

// Hover UI methods
function addHoverDom(treeId, treeNode) {
    var sObj = $("#" + treeNode.tId + "_span");
    if(treeNode.isParent){
        if (treeNode.editNameFlag || $("#addFileBtn_"+treeNode.tId).length>0) return;
        if (treeNode.editNameFlag || $("#addDirBtn_"+treeNode.tId).length>0) return;
        var addFileStr = "<span class='button add' id='addFileBtn_" + treeNode.tId
            + "' title='add file' onfocus='this.blur();'></span>";
        var addDirStr = "<span class='button folder' id='addDirBtn_" + treeNode.tId
            + "' title='add folder' onfocus='this.blur();'></span>";
        sObj.after(addDirStr);
        sObj.after(addFileStr);
        var btnFile = $("#addFileBtn_"+treeNode.tId);
        var btnDir = $("#addDirBtn_"+treeNode.tId);
        if (btnFile) btnFile.bind("click", function(){
            var zTree = $.fn.zTree.getZTreeObj("treeDemo");
            zTree.addNodes(treeNode, { name: `newFile`});
            zTree.editName(treeNode.children[treeNode.children.length-1]);
            return false;
        });
        if (btnDir) btnDir.bind("click", function(){
            var zTree = $.fn.zTree.getZTreeObj("treeDemo");
            zTree.addNodes(treeNode, { name: `newDir`, isParent: true});
            zTree.editName(treeNode.children[treeNode.children.length-1]);
            return false;
        });
    }
};

function removeHoverDom(treeId, treeNode) {
    $("#addFileBtn_"+treeNode.tId).unbind().remove();
    $("#addDirBtn_"+treeNode.tId).unbind().remove();
};

function showRemoveBtn(treeId, treeNode) {
    return treeNode.name !=  "main";
}

//Button Methods
function Save() {
    var program = editor.getValue();
    if (program !== ''){
        activeNode.program = program;
    }
}

function onRemove(e, treeId, treeNode) {
    RemoveFile(treeNode.fileId);
}

function onRename(e, treeId, treeNode) {
    var zTree = $.fn.zTree.getZTreeObj("treeDemo");
      if (treeNode.name.length == 0) {
        alert("file name can not be empty.");
        zTree.removeNode(treeNode);
      } else if (treeNode.name == 'main') {
        alert("file name can not be 'main'");
        zTree.removeNode(treeNode);
      } else {
        AddFile(treeNode);
      }
}


function onClick(e, treeId, treeNode) {
    Save();
    editor.setValue(treeNode.program);
    programDisplayed = treeNode.program;
    activeNode = treeNode;
}

// Cookie Method
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
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
    file_id = activeNode.fileId
    var form = new FormData();

    form.append("_method", "put");
    form.append("project_id", project_id);
    form.append("program", program);
    fetch(`http://127.0.0.1:8000/api/v1/file/${file_id}`,{
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
            "X-Requested-With": "XMLHttpRequest",
        }
    })
    .then(res => res.json())
    .then(data => {
            document.getElementById("output").innerHTML = data.output;
        }
    )
}

function AddFile(treeNode) {
    var form = new FormData();
    form.append("fileName", treeNode.name);
    fetch(`http://127.0.0.1:8000/api/v1/project/${project_id}`, {
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
            "X-Requested-With": "XMLHttpRequest",
        }
    })
}

function RemoveFile(fileIdd) {
    var form = new FormData();
    var fileId = fileIdd
    form.append("_method", "delete");
    fetch(`http://127.0.0.1:8000/api/v1/file/${fileId}`, {
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
            "X-Requested-With": "XMLHttpRequest",
        }
    })
}

//function OpenFile(treeNode) {
//    var form = new FormData();
//    form.append("fileName", treeNode.name);
//    fetch(`http://127.0.0.1:8000/api/v1/file/${fileId}`, {
//        method: "POST",
//        body: form,
//        headers: {
//            "X-CSRFToken": getCookie('csrftoken'),
//            "X-Requested-With": "XMLHttpRequest",
//        }
//    })
//}



