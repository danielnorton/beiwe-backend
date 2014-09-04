function graph(input){
plot1 = $.jqplot ('chart1', [input], {
        // Give the plot a title.
      title: 'Graph Of a question',
      animate: true,
      series:[{
            // Don't show a line, just show markers.
            // Make the markers 7 pixels with an 'x' style
            // showLine:false,
            markerOptions: { size: 10, style:"filledCircle" },
            pointLabels: {show: true},
            rendererOptions: {animation:{speed: 2000}},
            showLine: false
          }],
      // You can specify options for all axes on the plot at once with
      // the axesDefaults object.  Here, we're using a canvas renderer
      // to draw the axis label which allows rotated text.
      axesDefaults: {
        tickRenderer: $.jqplot.CanvasAxisTickRenderer,
        labelRenderer: $.jqplot.CanvasAxisLabelRenderer,
        tickOptions: {
          angle: -20,

        },
        labelOptions: {
            angle: -45
        }
      },
      // An axes object holds options for all axes.
      // Allowable axes are xaxis, x2axis, yaxis, y2axis, y3axis, ...
      // Up to 9 y axes are supported.
      axes: {
        // options for each axis are specified in seperate option objects.
        xaxis: {
          show: false,
          label: "X Axis",
          // Turn off "padding".  This will allow data point to lie on the
          // edges of the grid.  Default padding is 1.2 and will keep all
          // points inside the bounds of the grid.
          pad: 0
        },
        yaxis: {
            // showTicks : false,
            label: "Y Axis",
        },
      },
      seriesColors: ["#7BB661", "#E03C31"],
      highlighter: {
            show: true,
            showLabel: true,
            yvalues: 3,
            tooltipAxes: 'y',
            formatString: "%#.2f",
            sizeAdjust: 7.5 , tooltipLocation : 'ne'
        }
    });
}

function replot_user_results(question_number) {
    $('#chart1').empty();
    // TODO: Need to grab information specific to that question in the last X days.
    // For now, the question_number variable is useless
    var new_data =  [10 ,6.5 ,5.7 ,9 ,8.2];
    graph(new_data);
}

// $(document).ready(function() {
// graph([4, 6.5, 5.7 ,9 ,8.2]);
// });