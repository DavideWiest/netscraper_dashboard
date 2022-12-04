

Chart.defaults.RoundedDoughnut = Chart.helpers.clone(Chart.defaults.doughnut);
Chart.controllers.RoundedDoughnut = Chart.controllers.doughnut.extend({
    draw: function (ease) {
            var ctx = this.chart.chart.ctx;
        
        var easingDecimal = ease || 1;
        Chart.helpers.each(this.getDataset().metaData, function (arc, index) {
            arc.transition(easingDecimal).draw();

            var vm = arc._view;
            var radius = (vm.outerRadius + vm.innerRadius) / 2;
            var thickness = (vm.outerRadius - vm.innerRadius) / 2;
            var angle = Math.PI - vm.endAngle - Math.PI / 2;
            
            ctx.save();
            ctx.fillStyle = vm.backgroundColor;
            ctx.translate(vm.x, vm.y);
            ctx.beginPath();
            ctx.arc(radius * Math.sin(angle), radius * Math.cos(angle), thickness, 0, 2 * Math.PI);
            ctx.arc(radius * Math.sin(Math.PI), radius * Math.cos(Math.PI), thickness, 0, 2 * Math.PI);
            ctx.closePath();
            ctx.fill();
            ctx.restore();
        });
    },
});


var deliveredData = {
    labels: [
        "Value"
    ],
    datasets: [
        {
            data: [85, 15],
            backgroundColor: [
                "#3ec556",
                "rgba(0,0,0,0)"
            ],
            hoverBackgroundColor: [
                "#3ec556",
                "rgba(0,0,0,0)"
            ],
            borderWidth: [
                0, 0
            ]
        }]
};

var deliveredDataCPU = Object.assign({}, deliveredData);
deliveredDataCPU.datasets[0].data = [cpu_usage, 100-cpu_usage]
var deliveredDataGPU = Object.assign({}, deliveredData);
deliveredDataGPU.datasets[0].data = [gpu_usage, 100-gpu_usage]

var deliveredOpt = {
    cutoutPercentage: 88,
    animation: {
        animationRotate: true,
        duration: 2000
    },
    legend: {
        display: false
    },
    tooltips: {
        enabled: false
    }
};

function makechart1() {
    var gpuchart = new Chart($('#gpu_usage'), {
        type: 'RoundedDoughnut',
        data: deliveredDataGPU,
        options: deliveredOpt
    });
}

function makechart2() {
    var cpuchart = new Chart($('#cpu_usage'), {
        type: 'RoundedDoughnut',
        data: deliveredDataCPU,
        options: deliveredOpt
    });
}

makechart2()
makechart1()


