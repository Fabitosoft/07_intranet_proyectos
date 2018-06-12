import React, {Component, Fragment} from 'react';
import * as actions from "../../../../01_actions/01_index";
import {connect} from "react-redux";
import {fechaFormatoUno} from "../../../../00_utilities/common";
import CargarDatos from "../../../../00_utilities/components/system/cargar_datos";
import moment from 'moment-timezone';
import momentLocaliser from "react-widgets-moment";

moment.tz.setDefault("America/Bogota");
moment.locale('es');
momentLocaliser(moment);

import {Link} from 'react-router-dom'

const Tarea = (props) => {
    const {fecha, nombre, link_to} = props;
    const ahora = moment(new Date());
    const fecha_tarea = moment(fecha);
    const diferencia = fecha_tarea.diff(ahora, "days");
    let diferencia_texto = 'Hoy';
    let style = {color: 'black'};
    if (diferencia === 0) {
        style = {backgroundColor: 'green', color: 'white'};
    } else if (diferencia > 0) {
        diferencia_texto = `En ${diferencia} días`;
    } else {
        diferencia_texto = `Hace ${diferencia * -1} días`;
    }
    return (
        <Link to={link_to}>
            <li className="list-group-item" style={style}>
                {fechaFormatoUno(fecha)} - <strong>{nombre} </strong> ({diferencia_texto})
            </li>
        </Link>
    )
};

class SeguimientoTareasCotizacionesList extends Component {
    constructor(props) {
        super(props);
        this.cargarDatos = this.cargarDatos.bind(this);
    }

    componentWillUnmount() {
        this.props.clearSeguimientosCotizaciones();
        this.props.clearCotizaciones();
    }

    cargarDatos() {
        const {cargando, noCargando, notificarErrorAjaxAction} = this.props;
        cargando();
        const cargarCotizacionesAgendadas = () => this.props.fetchCotizacionesAgendadas(() => noCargando(), notificarErrorAjaxAction);
        this.props.fetchSeguimientosCotizacionesTareasPendientes(cargarCotizacionesAgendadas, notificarErrorAjaxAction);
    }

    componentDidMount() {
        this.cargarDatos()
    }

    render() {
        const {tareas_list, cotizaciones_agendas_list} = this.props;
        const listado_tareas = _.map(tareas_list, t => {
            return {
                fecha: t.fecha_inicio_tarea,
                nombre: t.nombre_tarea,
                cotizacion: t.cotizacion,
                key: `t-${t.cotizacion}-${t.id}`
            }
        });

        const listado_cotizaciones_agendadas = _.map(cotizaciones_agendas_list, c => {
            return {
                fecha: c.fecha_entrega_pactada_cotizacion,
                nombre: c.descripcion_cotizacion,
                cotizacion: c.id,
                key: `c-${c.id}`
            }
        });
        const listado_completo = _.orderBy([...listado_tareas, ...listado_cotizaciones_agendadas], ['fecha'], ['asc']);
        return (
            <div>
                {
                    listado_completo.length > 0 &&
                    <Fragment>
                        <h1>Tareas Cotizaciones</h1>
                        <ul className="list-group">
                            {listado_completo.map(t => {
                                return (
                                    <Tarea
                                        key={t.key}
                                        fecha={t.fecha}
                                        nombre={t.nombre}
                                        link_to={`/app/proyectos/cotizaciones/cotizaciones/detail/${t.cotizacion}`}
                                    />
                                )
                            })}
                        </ul>
                    </Fragment>

                }
                <CargarDatos
                    cargarDatos={this.cargarDatos}
                />
            </div>
        )
    }

}

function mapPropsToState(state, ownProps) {
    return {
        mis_permisos: state.mis_permisos,
        tareas_list: state.cotizaciones_seguimientos,
        cotizaciones_agendas_list: state.cotizaciones,
    }
}

export default connect(mapPropsToState, actions)(SeguimientoTareasCotizacionesList)