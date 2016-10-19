var w = $('#box').width();
var h = $('#box').height();
var x_ax=w/20;
var y_ax=h/20;
var board_atts = {
        boundingbox: [-x_ax, y_ax, x_ax, -y_ax],
        axis: true,
        showCopyright:false,
        showNavigation:false,
        pan: {
            enabled: true,
            needshift: false,
            needTwoFingers: true
        },
        zoom: {
            factorX: 1.25,
            factorY: 1.25,
            wheel: true,
            needshift: false
        }
    }

var plots = -1
    //A better function plotter
    //http://jsxgraph.uni-bayreuth.de/wiki/index.php/Even_simpler_function_plotter

//Use Board.removeObject() to delete individual lines
var lines = []

var board = JXG.JSXGraph.initBoard('box', board_atts);

function arg(x, y) {
    if (x > 0) {
        return Math.atan(y / x);
    } else if (x < 0 && y >= 0) {
        return Math.atan(y / x) + Math.PI;
    } else if (x < 0 && y < 0) {
        return Math.atan(y / x) - Math.PI;
    } else if (x === 0 && y > 0) {
        return Math.PI / 2;
    } else if (x === 0 && y < 0) {
        return -1 * Math.PI / 2;
    }
    return null
};

function addplot(){
var eq = $('input[name="in"]').val()
$.getJSON($SCRIPT_ROOT + '/_plot', {
    eq: eq
}, function(data) {
    plots += 1;
    lines.push([]);
    $('#expressions tbody').append(
        '<tr id="row'+plots+'">'+
            '<td>'+
                '`'+eq+'`'+
            '</td>'+
            '<td>'+
                '<input type="checkbox" name="plot" id="'+plots+'" checked>'+
            '</td>'+
            '<td>'+
                '<input type="button" class="btn btn-block" name="del" id="del'+plots+'" value="X">'+
            '</td>'+
        '</tr>'
        )
    MathJax.Hub.Queue(["Typeset",MathJax.Hub,"expressions"])
    if (data.type==='func'){
        $.each(data.result, function(i, v) {
            f = board.jc.snippet(v, true, 'x', true);
            curve = board.create('functiongraph', [f], {
                name: plots,
                strokeWidth:2,
                withLabel: false
            });
            lines[plots].push(curve);
        });
    } else if (data.type==='vert') {
        curve=board.create('line',[-data.result[0],1,0],{
            name: plots,
            strokeWidth:2,
            fixed: true,
            withLabel: false
        });
        lines[plots].push(curve);
    } else if (data.type=='ray'){
        p1=data.result[0]; //vertex
        p2=data.result[1];
        console.log(p1,p2)
        curve=board.create('line',[p1,p2],{
            straightFirst:false,
            fixed:true
            });
        lines[plots].push(curve);
    } else if (data.type=='arc') {

    }
});
return false;

}


$(document).ready(function() {
    $('#eq_in').on('keyup', function(e) {
        if (e.keyCode===13) {
            addplot();
        }});
    $('#go').on('click', addplot);
    $('#clear').on('click', function() {
        $('#expressions tbody > tr').remove();
        plots = -1;
        lines=[];
        JXG.JSXGraph.freeBoard(board);
        board = JXG.JSXGraph.initBoard('box', board_atts);
    });
    $('#expressions').on('click','[type=button]',function(){
        var id = $(this).attr('id').replace('del','');
        $.each(lines[id], function(i,v){
            board.removeObject(v);
        });
        lines[id]=[];
        $('#row'+id).remove();
    });
    $('#expressions').on('click','[type=checkbox]',function(){
        console.log(this);
        var id=$(this).attr('id')
        console.log(id,plots,lines[id]);
        $.each(lines[id], function(i,v){
            vis = !v.getAttribute('visible');
            v.setAttribute({visible:vis});
        });
    });

});
