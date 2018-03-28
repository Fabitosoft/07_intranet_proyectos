import React, {Component} from 'react';
import CreateForm from './forms/colaborador_form';
import Tabla from './colaboradores_tabla';
import crudHOC from '../../../../../../00_utilities/components/hoc_crud';


const CRUD = crudHOC(CreateForm, Tabla);

class List extends Component {
    constructor(props) {
        super(props);
        this.method_pool = {
            fetchObjectMethod: this.fetchObjectMethod.bind(this),
            deleteObjectMethod: this.deleteObjectMethod.bind(this),
            createObjectMethod: this.createObjectMethod.bind(this),
            updateObjectMethod: this.updateObjectMethod.bind(this),
        };
        this.plural_name = 'Colaboradores';
        this.singular_name = 'Colaborador';
        this.onCreateColaboradorUsuario = this.onCreateColaboradorUsuario.bind(this);
    }

    successSubmitCallback(item) {
        const nombre = `${item.nombres} ${item.apellidos}`;
        const {noCargando, notificarAction} = this.props;
        notificarAction(`Se ha ${item.id ? 'actualizado' : 'creado'} con éxito ${this.singular_name.toLowerCase()} ${nombre}`);
        noCargando()
    }


    successDeleteCallback(item) {
        const nombre = `${item.nombres} ${item.apellidos}`;
        const {noCargando, notificarAction} = this.props;
        notificarAction(`Se ha eliminado con éxito ${this.singular_name.toLowerCase()} ${nombre}`);
        noCargando()
    }

    fetchObjectMethod(item_id, successCallback) {
        const {cargando, noCargando, notificarErrorAjaxAction} = this.props;
        const success_method = (item) => {
            successCallback(item);
            noCargando();
        };
        cargando();
        this.props.fetchColaborador(item_id, success_method, notificarErrorAjaxAction);
    }

    createObjectMethod(item, successCallback) {
        const {cargando, notificarErrorAjaxAction} = this.props;
        const success_method = () => {
            this.successSubmitCallback(item);
            successCallback();
        };
        cargando();
        this.props.createColaborador(item, success_method, notificarErrorAjaxAction);
    }

    updateObjectMethod(item, successCallback) {
        const {cargando, notificarErrorAjaxAction} = this.props;
        const success_method = () => {
            this.successSubmitCallback(item);
            successCallback();
        };
        cargando();
        this.props.updateColaborador(item.id, item, success_method, notificarErrorAjaxAction);
    }

    deleteObjectMethod(item, successCallback) {
        const {cargando, notificarErrorAjaxAction} = this.props;
        const success_method = () => {
            this.successDeleteCallback(item);
            successCallback();
        };
        cargando();
        this.props.deleteColaborador(item.id, success_method, notificarErrorAjaxAction);
    }

    onCreateColaboradorUsuario(item) {
        const {cargando, noCargando, notificarErrorAjaxAction} = this.props;
        cargando();
        this.props.createColaboradorUsuario(
            item.id,
            (response) => {
                this.props.notificarAction(`Se ha creado el usuario ${response.usuario_username} para ${response.nombres} ${response.apellidos} con exitoso!`)
                noCargando();
            },
            notificarErrorAjaxAction
        )
    }

    render() {
        const {object_list, permisos_object} = this.props;
        return (
            <CRUD
                onCreateColaboradorUsuario={this.onCreateColaboradorUsuario}
                method_pool={this.method_pool}
                list={object_list}
                permisos_object={permisos_object}
                plural_name={this.plural_name}
                singular_name={this.singular_name}
                {...this.props}
            />
        )
    }
}

export default List;