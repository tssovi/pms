$(function() {

  // sparkline charts
  var sparklineNumberChart = function() {

    var params = {
      width: '140px',
      height: '30px',
      lineWidth: '2',
      lineColor: '#20B2AA',
      fillColor: false,
      spotRadius: '2',
      spotColor: false,
      minSpotColor: false,
      maxSpotColor: false,
      disableInteraction: false
    };

    $('#number-chart1').sparkline('html', params);
    $('#number-chart2').sparkline('html', params);
    $('#number-chart3').sparkline('html', params);
    $('#number-chart4').sparkline('html', params);
  };

  sparklineNumberChart();


  // traffic sources
  var dataPie = {
    series: [45, 25, 30]
  };

  var labels = ['Direct', 'Organic', 'Referral'];
  var sum = function(a, b) {
    return a + b;
  };

  new Chartist.Pie('#demo-pie-chart', dataPie, {
    height: "270px",
    labelInterpolationFnc: function(value, idx) {
      var percentage = Math.round(value / dataPie.series.reduce(sum) * 100) + '%';
      return labels[idx] + ' (' + percentage + ')';
    }
  });


  // progress bars
  $('.progress .progress-bar').progressbar({
    display_text: 'none'
  });

  // line chart
  var data = {
    labels: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
    series: [
      [200, 380, 350, 480, 410, 450, 550],
    ]
  };

  var options = {
    height: "200px",
    showPoint: true,
    showArea: true,
    axisX: {
      showGrid: false
    },
    lineSmooth: false,
    chartPadding: {
      top: 0,
      right: 0,
      bottom: 30,
      left: 30
    },
    plugins: [
      Chartist.plugins.tooltip({
        appendToBody: true
      }),
      Chartist.plugins.ctAxisTitle({
        axisX: {
          axisTitle: 'Day',
          axisClass: 'ct-axis-title',
          offset: {
            x: 0,
            y: 50
          },
          textAnchor: 'middle'
        },
        axisY: {
          axisTitle: 'Reach',
          axisClass: 'ct-axis-title',
          offset: {
            x: 0,
            y: -10
          },
        }
      })
    ]
  };

  new Chartist.Line('#demo-line-chart', data, options);


  // sales performance chart
  var sparklineSalesPerformance = function() {

    var lastWeekData = [142, 164, 298, 384, 232, 269, 211];
    var currentWeekData = [352, 267, 373, 222, 533, 111, 60];

    $('#chart-sales-performance').sparkline(lastWeekData, {
      fillColor: 'rgba(90, 90, 90, 0.1)',
      lineColor: '#5A5A5A',
      width: '' + $('#chart-sales-performance').innerWidth() + '',
      height: '100px',
      lineWidth: '2',
      spotColor: false,
      minSpotColor: false,
      maxSpotColor: false,
      chartRangeMin: 0,
      chartRangeMax: 1000
    });

    $('#chart-sales-performance').sparkline(currentWeekData, {
      composite: true,
      fillColor: 'rgba(60, 137, 218, 0.1)',
      lineColor: '#3C89DA',
      lineWidth: '2',
      spotColor: false,
      minSpotColor: false,
      maxSpotColor: false,
      chartRangeMin: 0,
      chartRangeMax: 1000
    });
  }

  sparklineSalesPerformance();

  var sparkResize;
  $(window).on('resize', function() {
    clearTimeout(sparkResize);
    sparkResize = setTimeout(sparklineSalesPerformance, 200);
  });


  // top products
  var dataStackedBar = {
    labels: ['Q1', 'Q2', 'Q3'],
    series: [
      [800000, 1200000, 1400000],
      [200000, 400000, 500000],
      [100000, 200000, 400000]
    ]
  };

  new Chartist.Bar('#chart-top-products', dataStackedBar, {
    height: "250px",
    stackBars: true,
    axisX: {
      showGrid: false
    },
    axisY: {
      labelInterpolationFnc: function(value) {
        return (value / 1000) + 'k';
      }
    },
    plugins: [
      Chartist.plugins.tooltip({
        appendToBody: true
      }),
      Chartist.plugins.legend({
        legendNames: ['Phone', 'Laptop', 'PC']
      })
    ]
  }).on('draw', function(data) {
    if (data.type === 'bar') {
      data.element.attr({
        style: 'stroke-width: 30px'
      });
    }
  });


  // notification popup
  // toastr.options.closeButton = true;
  // toastr.options.positionClass = 'toast-bottom-right';
  // toastr.options.showDuration = 1000;
  // toastr['info']('Hello, Welcome To MoneyBook, A Complete Accounting Software.');
  // $("#password-f").password('toggle');
  // $("#password").password('toggle');
    $("#showHidePF").click(function () {
        if ($("#password-f").attr("type") == "password") {
            $("#password-f").attr("type", "text");
            $("#showHideIconPF").removeClass("fa-eye");
            $("#showHideIconPF").addClass("fa-eye-slash");

        } else {
            $("#password-f").attr("type", "password");
            $("#showHideIconPF").removeClass("fa-eye-slash");
            $("#showHideIconPF").addClass("fa-eye");
        }
    });
    $("#showHideP").click(function () {
        if ($("#password").attr("type") == "password") {
            $("#password").attr("type", "text");
            $("#showHideIconP").removeClass("fa-eye");
            $("#showHideIconP").addClass("fa-eye-slash");

        } else {
            $("#password").attr("type", "password");
            $("#showHideIconP").removeClass("fa-eye-slash");
            $("#showHideIconP").addClass("fa-eye");
        }
    });
  $("#food").select2({
      allowClear: true
  });

  $('#payment-create-form, #register-form, #password-update-form, #acn-create-form, #bank-create-form, #customer-create-form').parsley();

  $('#regdate').datepicker({
    todayHighlight: true
  });

  // $('#acn_start_date').datepicker({
  //   todayHighlight: true
  // });
  //
  // $('#acn_end_date').datepicker({
  //   todayHighlight: true
  // });

  $('#phone, #phone_no').mask('8801999999999');
  $('#attachmentFile, #userAvatar').dropify();

  var payment = $('#datatable_payment').DataTable({
        "columnDefs": [{
            "searchable": false,
            "orderable": false,
            "targets": 0,
        },
        {
            "targets": 0,
            "className": "text-center",
        },
        {
            "targets": 1,
            "className": "text-center",
        },
        {
            "targets": 2,
            "className": "text-center",
        },
        {
            "targets": 3,
            "className": "text-center",
        },
        {
            "targets": 4,
            "className": "text-center",
        },
        {
            "targets": 5,
            "className": "text-center",
        },
        {
            "targets": 6,
            "className": "text-center",
        },
        {
            "targets": 7,
            "className": "text-center",
        },
        {
            "targets": 8,
            "className": "text-center",
        },
        {
            "targets": 9,
            "className": "text-center",
        }],
        "order": [[0, 'asc']],
        "responsive": true,
        "language": {
            "lengthMenu": "Show _MENU_ Entries",
            "zeroRecords": "No Data Found ...",
            "sInfo": "Showing _START_ To _END_ Of _TOTAL_ Entries",
            "sInfoEmpty": "Showing 0 To 0 Of 0 Entries",
            "infoFiltered": "(Filtered From _MAX_ Total Records)"
        }
    });

  payment.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();

  var account = $('#datatable_acn').DataTable({
        "columnDefs": [{
            "searchable": false,
            "orderable": false,
            "targets": 0,
        },
        {
            "targets": 0,
            "className": "text-center",
        },
        {
            "targets": 1,
            "className": "text-center",
        },
        {
            "targets": 2,
            "className": "text-center",
        },
        {
            "targets": 3,
            "className": "text-center",
        }],
        "buttons": [
            'copy', 'csv', 'excel', 'pdf', 'print'
        ],
        "order": [[0, 'asc']],
        "language": {
            "lengthMenu": "Show _MENU_ Entries",
            "zeroRecords": "No Data Found ...",
            "sInfo": "Showing _START_ To _END_ Of _TOTAL_ Entries",
            "sInfoEmpty": "Showing 0 To 0 Of 0 Entries",
            "infoFiltered": "(Filtered From _MAX_ Total Records)"
        }
    });

  account.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();

  var customer = $('#datatable_customer').DataTable({
        "columnDefs": [{
            "searchable": false,
            "orderable": false,
            "targets": 0,
        },
        {
            "targets": 0,
            "className": "text-center",
        },
        {
            "targets": 1,
            "className": "text-center",
        },
        {
            "targets": 2,
            "className": "text-center",
        },
        {
            "targets": 3,
            "className": "text-center",
        },
        {
            "targets": 4,
            "className": "text-center",
        },
        {
            "targets": 5,
            "className": "text-center",
        },
        {
            "targets": 6,
            "className": "text-center",
        }],
        "order": [[0, 'asc']],
        "language": {
            "lengthMenu": "Show _MENU_ Entries",
            "zeroRecords": "No Data Found ...",
            "sInfo": "Showing _START_ To _END_ Of _TOTAL_ Entries",
            "sInfoEmpty": "Showing 0 To 0 Of 0 Entries",
            "infoFiltered": "(Filtered From _MAX_ Total Records)"
        }
    });

  customer.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();

  var bank = $('#datatable_bank').DataTable({
        "columnDefs": [{
            "searchable": false,
            "orderable": false,
            "targets": 0,
        },
        {
            "targets": 0,
            "className": "text-center",
        },
        {
            "targets": 1,
            "className": "text-center",
        },
        {
            "targets": 2,
            "className": "text-center",
        },
        {
            "targets": 3,
            "className": "text-center",
        },
        {
            "targets": 4,
            "className": "text-center",
        },
        {
            "targets": 5,
            "className": "text-center",
        }],
        "order": [[0, 'asc']],
        "language": {
            "lengthMenu": "Show _MENU_ Entries",
            "zeroRecords": "No Data Found ...",
            "sInfo": "Showing _START_ To _END_ Of _TOTAL_ Entries",
            "sInfoEmpty": "Showing 0 To 0 Of 0 Entries",
            "infoFiltered": "(Filtered From _MAX_ Total Records)"
        }
    });

  bank.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
            cell.innerHTML = i+1;
        } );
    } ).draw();
});
