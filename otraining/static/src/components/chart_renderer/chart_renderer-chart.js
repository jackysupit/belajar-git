/** @odoo-module */

import { registry } from "@web/core/registry"
import { loadJS } from "@web/core/assets"
const { Component, onWillStart, useRef, onMounted } = owl

export class ChartRenderer extends Component {
    setup(){
        this.chartRef = useRef("chart")
        onWillStart(async ()=>{
            await loadJS("https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js");
            // await loadJS('http://localhost:4010/odoo_custom_dashboard/static/lib/apexcharts-bundle/dist/apexcharts.min.js');
        })

        onMounted(()=>this.renderChart())
    }


    renderChart(){
        const chart_type = this.props.type;


        let data_doughnut = {
			labels: ['Maritime Cyber Security', 'DPA ISM Code', 'IMDG Code'],
			datasets: [
				{
					label: 'Penghasilan Training',
					data: [30000000, 5000000, 10000000],
					backgroundColor: [
						'rgb(255, 99, 132)',
						'rgb(54, 162, 235)',
						'rgb(255, 205, 86)',
					],
					hoverOffset: 4,
				},
			],
		};

        let data_pie = {
			labels: ['Aktif', 'Tidak Aktif', 'Belum Konfirmasi'],
			datasets: [
				{
					label: 'Jumlah Peserta',
					data: [100, 50, 30],
					backgroundColor: [
						'rgb(255, 99, 132)',
						'rgb(54, 162, 235)',
						'rgb(255, 205, 86)',
					],
					hoverOffset: 4,
				},
			],
		};        

        let data_bar = {
			labels: ['Minggu 1', 'Minggu 2', 'Minggu 3'],
			datasets: [
				{
					label: 'Bulan Lalu',
					data: [300, 50, 100],
					hoverOffset: 4,
				},
				{
					label: 'Bulan Ini',
					data: [100, 70, 150],
					hoverOffset: 4,
				},
			],
		};

    const plugin_doughnut = {
		id: 'customCanvasBackgroundColor',
		beforeDraw: (chart, args, options) => {
			const { ctx } = chart;
			ctx.save();
			ctx.globalCompositeOperation = 'destination-over';
			ctx.fillStyle = options.color || '#99ffff';
			ctx.fillRect(0, 0, chart.width, chart.height);
			ctx.restore();
		},
	};

        let option_all = {
			responsive: true,
			plugins: {
				legend: {
					position: 'bottom',
				},
				title: {
					display: true,
					text: this.props.title,
					position: 'bottom',
				},
				id: 'customCanvasBackgroundColor',
				beforeDraw: (chart, args, options) => {
					const { ctx } = chart;
					ctx.save();
					ctx.globalCompositeOperation = 'destination-over';
					ctx.fillStyle = options.color || '#99ffff';
					ctx.fillRect(0, 0, chart.width, chart.height);
					ctx.restore();
				},
			},
		};
        if (chart_type) {
            option_all['tooltips'] = {
                tooltips: {
                    callbacks: {
                        label: function(tooltipItem, data) {
                            var dataset = data.datasets[tooltipItem.datasetIndex];
                            var total = dataset.data.reduce(function(previousValue, currentValue, currentIndex, array) {
                                return previousValue + currentValue;
                            });
                            var currentValue = dataset.data[tooltipItem.index];
                            var percentage = Math.floor(((currentValue/total) * 100)+0.5);         
                            return percentage + "%";
                        }
                    }
                }
            }
        }

        let data = data_bar;
        if(chart_type == 'pie') data = data_pie
        else if(chart_type == 'doughnut') data = data_doughnut

        let config = {
			type: chart_type,
			data: data,
			options: option_all,
		};

        if(chart_type == 'doughnut') {
            config = {
                type: 'doughnut',
                data: data_doughnut,
                options: {
                    plugins: {
                        customCanvasBackgroundColor: {
                            color: 'lightGreen',
                        },
                    },
                },
                plugins: [plugin_doughnut],
            };            
        }

        new Chart(this.chartRef.el, config);
    }
}

ChartRenderer.template = "owl.ChartRenderer"