var board_atts={boundingbox:[-6,6,6,-6],
    axis:true,
    pan:{enabled:true,
        needshift:false,
        needTwoFingers:true
        },
    zoom:{
        factorX:1.25,
        factorY:1.25,
        wheel:true,
        needshift:false
        }
    }
//var board = JXG.JSXGraph.initBoard('box', board_atts);

var plots = 0 //Use plots variable to track each plot (name of each curve)
//A better function plotter
//http://jsxgraph.uni-bayreuth.de/wiki/index.php/Even_simpler_function_plotter

//Hide/show elements from checkboxes
//https://groups.google.com/forum/#!topic/jsxgraph/-AAkjV4CTDw

//Use Board.removeObject() to delete individual lines

var board = JXG.JSXGraph.initBoard('box', board_atts);

$(document).ready(function(){
    $('#go').on('click',function(){
        console.log(board);
        var input=$('#eq_in').val();
        f=board.jc.snippet(input,true,'x',true);
        curve=board.create('functiongraph',[f],{name:input,withLabel:true});
        plots+=1;
    });
    $('button#clear').on('click',function(){
        plots=0;
        JXG.JSXGraph.freeBoard(board);
        board = JXG.JSXGraph.initBoard('box', board_atts);
    });
});
