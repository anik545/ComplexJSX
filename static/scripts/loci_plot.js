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
    }}

var board = JXG.JSXGraph.initBoard('box', board_atts);

// Macro function plotter
function addCurve(board, func, atts) {
  var f = board.create('functiongraph', [func], atts);
  return f;
}

// Simplified plotting of function
function plot(func, atts) {
 if (atts==null) {
    return addCurve(board, func, {strokewidth:2});
 } else {
    return addCurve(board, func, atts);
 }
}

// Usage of the macro
function doIt() {
    function f(x){return eval(document.getElementById('eq_in').value);}
    c=plot(f);
    //eval(document.getElementById('eq_in').value);
    console.log('a');
}

function clearAll(board) {
    JXG.JSXGraph.freeBoard(board);

    var board = JXG.JSXGraph.initBoard('box', board_atts);
    return board;
}
