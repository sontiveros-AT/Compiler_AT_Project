<!--
        var setting = {
            view: {
                addHoverDom: addHoverDom,
                removeHoverDom: removeHoverDom,
                selectedMulti: false
            },
            check: {
                enable: true
            },
            data: {
                simpleData: {
                    enable: true
                }
            },
            edit: {
                enable: true
            }
        };

        var zNodes =[
            { id:1, pId:0, name:"pNode 1", open:true},
            { id:11, pId:1, name:"pNode 11"},
            { id:111, pId:11, name:"sNode 111"},
            { id:112, pId:11, name:"sNode 112"},
            { id:113, pId:11, name:"sNode 113"},
            { id:114, pId:11, name:"sNode 114"},
            { id:12, pId:1, name:"pNode 12"},
            { id:121, pId:12, name:"sNode 121"},
            { id:122, pId:12, name:"sNode 122"},
            { id:123, pId:12, name:"sNode 123"},
            { id:124, pId:12, name:"sNode 124"},
            { id:13, pId:1, name:"pNode 13", isParent:true},
            { id:2, pId:0, name:"pNode 2"},
            { id:21, pId:2, name:"pNode 21", open:true},
            { id:211, pId:21, name:"sNode 211"},
            { id:212, pId:21, name:"sNode 212"},
            { id:213, pId:21, name:"sNode 213"},
            { id:214, pId:21, name:"sNode 214"},
            { id:22, pId:2, name:"pNode 22"},
            { id:221, pId:22, name:"sNode 221"},
            { id:222, pId:22, name:"sNode 222"},
            { id:223, pId:22, name:"sNode 223"},
            { id:224, pId:22, name:"sNode 224"},
            { id:23, pId:2, name:"pNode 23"},
            { id:231, pId:23, name:"sNode 231"},
            { id:232, pId:23, name:"sNode 232"},
            { id:233, pId:23, name:"sNode 233"},
            { id:234, pId:23, name:"sNode 234"}
        ];

        $(document).ready(function(){
            $.fn.zTree.init($("#treeDemo"), setting, zNodes);
        });

        var newCount = 1;
        function addHoverDom(treeId, treeNode) {
            var sObj = $("#" + treeNode.tId + "_span");
            if (treeNode.editNameFlag || $("#addBtn_"+treeNode.tId).length>0) return;
            var addStr = "<span class='button add' id='addBtn_" + treeNode.tId
                + "' title='add node' onfocus='this.blur();'></span>";
            sObj.after(addStr);
            var btn = $("#addBtn_"+treeNode.tId);
            if (btn) btn.bind("click", function(){
                var zTree = $.fn.zTree.getZTreeObj("treeDemo");
                zTree.addNodes(treeNode, {id:(100 + newCount), pId:treeNode.id, name:"new node" + (newCount++)});
                return false;
            });
        };
        function removeHoverDom(treeId, treeNode) {
            $("#addBtn_"+treeNode.tId).unbind().remove();
        };
        //-->