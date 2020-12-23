// @editor.js Copyright (c) 2020 Jalasoft.
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
var editor = ace.edit("editor");
editor.setTheme("ace/theme/github");

// Ip Dom Origin
ip = "192.168.33.60";
port = "8000";

// get current project id
url = window.location.href.split("/");
project_id = url[url.length - 1];

var json = fetch(`http://${ip}:${port}/api/v1/project/json/${project_id}`)
    .then((res) => res.json())
    .then((data) => {
        editor.session.setMode(`ace/mode/${data.languageName}`);
        var zNodes = data.content;
        $(document).ready(function () {
            $.fn.zTree.init($("#treeDemo"), setting, zNodes);
        });
    })
    .catch((error) => console.log(error));
