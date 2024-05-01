/** @odoo-module */

import { registry } from "@web/core/registry"
import { KpiCard } from "./kpi_card/kpi_card"
import { ChartRenderer } from "./chart_renderer/chart_renderer"
import { loadJS } from "@web/core/assets"
const { Component, onWillStart, useRef, onMounted } = owl

export class OwlBKIDashboard extends Component {
    setup(){

    }
}

OwlBKIDashboard.template = "owl.OwlBKIDashboard"
OwlBKIDashboard.components = { KpiCard, ChartRenderer }

registry.category("actions").add("owl.bki_dashboard", OwlBKIDashboard)