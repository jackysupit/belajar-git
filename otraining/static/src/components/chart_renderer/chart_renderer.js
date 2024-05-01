/** @odoo-module */

import { registry } from "@web/core/registry"
import { loadJS } from "@web/core/assets"
const { Component, onWillStart, useRef, onMounted } = owl

export class ChartRenderer extends Component {
    setup(){
        this.chartRef = useRef("chart")
        onWillStart(async ()=>{
            await loadJS(
				'http://localhost:4010/odoo_custom_dashboard/static/lib/chartjs4/chart4.js'
			);
            await loadJS(
				'http://localhost:4010/odoo_custom_dashboard/static/lib/chartjs4/chart4-label.js'
			);
        })

        onMounted(()=>this.renderChart())
    }

    renderChart(){
        const chart_type = this.props.type;


        let data_donut = {
			labels: ['Maritime Cyber Security', 'DPA ISM Code', 'IMDG Code'],
			datasets: [
				{
					label: 'Penjualan Bulan Lalu',
					data: [300, 50, 100],
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
			labels: [
				'Jan',
				'Feb',
				'Mar',
				'Apr',
				'Mei',
				'Jun',
				'Jul',
				'Agu',
				'Sep',
				'Okt',
				'Nov',
				'Des',
			],
			datasets: [
				{
					label: '2023',
					data: [
						300, 50, 100, 200, 150, 175, 200, 400, 500, 300, 250,
						300,
					],
					hoverOffset: 4,
				},
				{
					label: '2024',
					data: [
						200, 150, 200, 150, 20, 0, 0, 0, 0, 0, 0,
						0,
					],
					hoverOffset: 4,
				},
			],
		};

        let data_bar_line = {
			labels: [
				'Jan',
				'Feb',
				'Mar',
				'Apr',
				'Mei',
				'Jun',
				'Jul',
				'Agu',
				'Sep',
				'Okt',
				'Nov',
				'Des',
			],
			datasets: [
				{
					label: '2023',
					data: [
						300, 50, 100, 200, 150, 175, 200, 400, 500, 300, 250,
						300,
					],
					type: 'line', // Set the type to line for this dataset
					fill: false, // Line chart specific options
					borderColor: 'rgba(54, 162, 235, 1)', // Line chart specific options
					borderWidth: 1, // Line chart specific options
				},
				{
					label: '2023',
					data: [
						300, 50, 100, 200, 150, 175, 200, 400, 500, 300, 250,
						300,
					],
					backgroundColor: 'rgba(255, 99, 132, 0.2)', // Bar chart specific options
					borderColor: 'rgba(255, 99, 132, 1)', // Bar chart specific options
					hoverOffset: 4,
				},
				{
					label: '2024',
					data: [200, 150, 200, 150, 20, 0, 0, 0, 0, 0, 0, 0],
					backgroundColor: 'rgba(255, 99, 132, 0.2)', // Bar chart specific options
					borderColor: 'rgba(100, 52, 200, 1)', // Bar chart specific options
					hoverOffset: 4,
				},
			],
		};

        let data_all = {
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
			ctx.fillStyle = options.color || 'pink' || '#99ffff';
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
			},
		};

        let option_pie = {
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
                customCanvasBackgroundColor: {
                    color: 'red',
                },
                labels: {
                    render: function (args) {
                        if(chart_type == 'pie') {
                            return `${args.value}\n${args.percentage}%`;
                        } else {
                            return '';
                        }
                    },
                },
            },
		};        

        if (false && chart_type) {
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

        let data = data_all;
        if(chart_type == 'pie') {
            data = data_pie;            
        }
        else if(chart_type == 'bar') {
            data = data_bar_line;
        } else if(chart_type == 'doughnut') {
            data = data_donut;
        }

        let options = option_all;
        // if (['pie', 'doughnut', 'line',].indexOf(chart_type) !== false) {


        let config = {
			type: chart_type,
			data: data,
			options: options,
		};

        let config_pie = {
			type: chart_type,
			data: data,
			options: option_pie,
		};

        if(chart_type == 'custom_plugin') {
            config = {
				type: chart_type,
				data: data_donut,
				options: {
					plugins: {
						customCanvasBackgroundColor: {
							color: 'red',
						}
					},
				},
				plugins: [plugin_doughnut],
			};
        }

        const el = this.chartRef.el;

        if (['pie'].indexOf(chart_type) !== false) {
            new Chart(el, config_pie);
		} else {
            new Chart(el, config);
        }

    }
}

ChartRenderer.template = "owl.ChartRenderer"