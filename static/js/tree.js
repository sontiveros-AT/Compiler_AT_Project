//var setting = {
//    view: {
//        addHoverDom: addHoverDom,
//        removeHoverDom: removeHoverDom,
//        selectedMulti: false
//    },
//    check: {
//        enable: true
//    },
//    data: {
//        simpleData: {
//            enable: true
//        }
//    },
//    edit: {
//        enable: true
//    }
//};
//
//
//
//var zNodes =[
//    { id:1, pId:0, name:"pNode 1", open:true},
//    { id:11, pId:1, name:"pNode 11"},
//    { id:111, pId:11, name:"sNode 111"},
//    { id:112, pId:11, name:"sNode 112"},
//    { id:113, pId:11, name:"sNode 113"},
//    { id:114, pId:11, name:"sNode 114"},
//    { id:12, pId:1, name:"pNode 12"},
//    { id:121, pId:12, name:"sNode 121"},
//    { id:122, pId:12, name:"sNode 122"},
//    { id:123, pId:12, name:"sNode 123"},
//    { id:124, pId:12, name:"sNode 124"},
//    { id:13, pId:1, name:"pNode 13", isParent:true}
//];
//
//$(document).ready(function(){
//    $.fn.zTree.init($("#treeDemo"), setting, zNodes);
//});
//
//var newCount = 1;
//function addHoverDom(treeId, treeNode) {
//    var sObj = $("#" + treeNode.tId + "_span");
//    if (treeNode.editNameFlag || $("#addBtn_"+treeNode.tId).length>0) return;
//    var addStr = "<span class='button add' id='addBtn_" + treeNode.tId
//        + "' title='add node' onfocus='this.blur();'></span>";
//    sObj.after(addStr);
//    var btn = $("#addBtn_"+treeNode.tId);
//    if (btn) btn.bind("click", function(){
//        var zTree = $.fn.zTree.getZTreeObj("treeDemo");
//        zTree.addNodes(treeNode, {id:(100 + newCount), pId:treeNode.id, name:"new node" + (newCount++)});
//        return false;
//    });
//};
//function removeHoverDom(treeId, treeNode) {
//    $("#addBtn_"+treeNode.tId).unbind().remove();
//};
////-->
//function test(){
//    //alert("Hola");
//    url = location.pathname;
//    document.getElementById('test1').value = url;
//    //data_from_django = {{ my_data }};
//    //widget.init(data_from_django);
//    //document.getElementById('test1').value = {{ my_data }};
//    //console.log(data_from_django);
//}

//var json = fetch(`http://127.0.0.1:8000/api/v1/file/${project_id}`)
//    .then(res => res.json())
//    .then(data => {
//        program = data.program;
//        console.log(data);
//        var zNodes =[
//			{ name: data.project_name, open:true, isParent: true,
//				children: [
//					{ name: `${data.files.file_name}${data.language.language_extension}`, fileId: `${data.files.id_file}`},
//					{ name: `newFile11`, fileId: `53`},
//					{ name: `newFile12`, fileId: `54`}
//		        ]
//		    }
//		];
//        editor.setValue(program);
//        $(document).ready(function(){
//            $.fn.zTree.init($("#treeDemo"), setting, zNodes);
//        });
//
//    })
//    .catch(error => console.log(error))