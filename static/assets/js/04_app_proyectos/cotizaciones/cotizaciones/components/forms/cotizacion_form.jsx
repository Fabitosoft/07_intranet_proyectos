import React, {Component} from 'react';
import {reduxForm} from 'redux-form';
import {connect} from "react-redux";
import {MyFormTagModal} from '../../../../../00_utilities/components/ui/forms/MyFormTagModal';
import validate from './validate';
import FormBaseCotizacion from '../forms/base_cotizacion_form';
import {formValueSelector} from 'redux-form';

const selector = formValueSelector('cotizacionForm');

class Form extends Component {
    componentDidMount() {
        this.props.fetchClientes();
    }

    componentWillUnmount() {
        this.props.clearClientes();
    }

    render() {
        const {
            pristine,
            submitting,
            reset,
            initialValues,
            onSubmit,
            onCancel,
            handleSubmit,
            modal_open,
            singular_name,
            clientes_list,
            myValues,
        } = this.props;
        const {estado} = myValues;
        const en_proceso = estado && estado !== 'Pendiente' && estado !== 'Aplazado' && estado !== 'Perdido';
        const esta_aprobado = estado === 'Aprobado';
        const enviado = estado && en_proceso && estado !== 'En Proceso';
        return (
            <MyFormTagModal
                onCancel={onCancel}
                onSubmit={handleSubmit(onSubmit)}
                reset={reset}
                initialValues={initialValues}
                submitting={submitting}
                modal_open={modal_open}
                pristine={pristine}
                element_type={singular_name}
            >
                <FormBaseCotizacion
                    item={initialValues}
                    en_proceso={en_proceso}
                    esta_aprobado={esta_aprobado}
                    enviado={enviado}
                    clientes_list={clientes_list}
                />
                <div style={{height: '300px'}}>

                </div>
            </MyFormTagModal>
        )
    }
}

function mapPropsToState(state, ownProps) {
    const {item_seleccionado} = ownProps;
    return {
        myValues: selector(state, 'estado', 'valor_ofertado'),
        initialValues: item_seleccionado,
    }
}

Form = reduxForm({
    form: "cotizacionForm",
    validate,
    enableReinitialize: true
})(Form);

Form = (connect(mapPropsToState, null)(Form));

export default Form;