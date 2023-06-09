"use strict";
window.chartColors = {green: "#75c181", blue: "#5b99ea", gray: "#a9b5c9", text: "#252930", border: "#e7e9ed"};
var randomDataPoint = function () {
    return Math.round(Math.random() * 100)
};
var lineChartConfig = {
    type: "line",
    data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
        datasets: [{
            label: "Dataset",
            backgroundColor: "rgba(117,193,129,0.2)",
            borderColor: "rgba(117,193,129, 0.8)",
            data: [randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint()],
        }]
    },
    options: {
        responsive: true,
        legend: {display: true, position: "bottom", align: "end",},
        tooltips: {
            mode: "index",
            intersect: false,
            titleMarginBottom: 10,
            bodySpacing: 10,
            xPadding: 16,
            yPadding: 16,
            borderColor: window.chartColors.border,
            borderWidth: 1,
            backgroundColor: "#fff",
            bodyFontColor: window.chartColors.text,
            titleFontColor: window.chartColors.text,
            callbacks: {
                label: function (b, a) {
                    return b.value + "%"
                }
            },
        },
        hover: {mode: "nearest", intersect: true},
        scales: {
            xAxes: [{
                display: true,
                gridLines: {drawBorder: false, color: window.chartColors.border,},
                scaleLabel: {display: false,}
            }],
            yAxes: [{
                display: true,
                gridLines: {drawBorder: false, color: window.chartColors.border,},
                scaleLabel: {display: false,},
                ticks: {
                    beginAtZero: true, userCallback: function (b, a, c) {
                        return b.toLocaleString() + "%"
                    }
                },
            }]
        }
    }
};
var barChartConfig = {
    type: "bar",
    data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
        datasets: [{
            label: "Dataset 1",
            backgroundColor: "rgba(117,193,129,0.8)",
            hoverBackgroundColor: "rgba(117,193,129,1)",
            data: [randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint()]
        }, {
            label: "Dataset 2",
            backgroundColor: "rgba(91,153,234,0.8)",
            hoverBackgroundColor: "rgba(91,153,234,1)",
            data: [randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint(), randomDataPoint()]
        }]
    },
    options: {
        responsive: true,
        legend: {position: "bottom", align: "end",},
        tooltips: {
            mode: "index",
            intersect: false,
            titleMarginBottom: 10,
            bodySpacing: 10,
            xPadding: 16,
            yPadding: 16,
            borderColor: window.chartColors.border,
            borderWidth: 1,
            backgroundColor: "#fff",
            bodyFontColor: window.chartColors.text,
            titleFontColor: window.chartColors.text,
            callbacks: {
                label: function (b, a) {
                    return b.value + "%"
                }
            },
        },
        scales: {
            xAxes: [{display: true, gridLines: {drawBorder: false, color: window.chartColors.border,},}],
            yAxes: [{
                display: true,
                gridLines: {drawBorder: false, color: window.chartColors.borders,},
                ticks: {
                    beginAtZero: true, userCallback: function (b, a, c) {
                        return b + "%"
                    }
                },
            }]
        }
    }
};
var pieChartConfig = {
    type: "pie",
    data: {
        datasets: [{
            data: [randomDataPoint(), randomDataPoint(), randomDataPoint(),],
            backgroundColor: [window.chartColors.green, window.chartColors.blue, window.chartColors.gray,],
            label: "Dataset 1"
        }], labels: ["Green", "Blue", "Gray",]
    },
    options: {
        responsive: true,
        legend: {display: true, position: "bottom", align: "center",},
        tooltips: {
            titleMarginBottom: 10,
            bodySpacing: 10,
            xPadding: 16,
            yPadding: 16,
            borderColor: window.chartColors.border,
            borderWidth: 1,
            backgroundColor: "#fff",
            bodyFontColor: window.chartColors.text,
            titleFontColor: window.chartColors.text,
            callbacks: {
                label: function (e, b) {
                    var c = b.datasets[e.datasetIndex];
                    var f = c.data.reduce(function (j, i, h, g) {
                        return j + i
                    });
                    var a = c.data[e.index];
                    var d = Math.floor(((a / f) * 100) + 0.5);
                    return d + "%"
                },
            },
        },
    }
};
var doughnutChartConfig = {
    type: "doughnut",
    data: {
        datasets: [{
            data: [randomDataPoint(), randomDataPoint(), randomDataPoint(),],
            backgroundColor: [window.chartColors.green, window.chartColors.blue, window.chartColors.gray,],
            label: "Dataset 1"
        }], labels: ["Green", "Blue", "Gray",]
    },
    options: {
        responsive: true,
        legend: {display: true, position: "bottom", align: "center",},
        tooltips: {
            titleMarginBottom: 10,
            bodySpacing: 10,
            xPadding: 16,
            yPadding: 16,
            borderColor: window.chartColors.border,
            borderWidth: 1,
            backgroundColor: "#fff",
            bodyFontColor: window.chartColors.text,
            titleFontColor: window.chartColors.text,
            animation: {animateScale: true, animateRotate: true},
            callbacks: {
                label: function (e, b) {
                    var c = b.datasets[e.datasetIndex];
                    var f = c.data.reduce(function (j, i, h, g) {
                        return j + i
                    });
                    var a = c.data[e.index];
                    var d = Math.floor(((a / f) * 100) + 0.5);
                    return d + "%"
                },
            },
        },
    }
};
window.addEventListener("load", function () {
    var c = document.getElementById("chart-line").getContext("2d");
    window.myLine = new Chart(c, lineChartConfig);
    var a = document.getElementById("chart-bar").getContext("2d");
    window.myBar = new Chart(a, barChartConfig);
    var d = document.getElementById("chart-pie").getContext("2d");
    window.myPie = new Chart(d, pieChartConfig);
    var b = document.getElementById("chart-doughnut").getContext("2d");
    window.myDoughnut = new Chart(b, doughnutChartConfig)
});