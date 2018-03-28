import React, {Component} from 'react';
import {reduxForm} from 'redux-form';
import {
    MyCombobox,
    MyDateTimePickerField
} from '../../../../../00_utilities/components/ui/forms/fields';
import {connect} from "react-redux";
import {MyFormTagModal} from '../../../../../00_utilities/components/ui/forms/MyFormTagModal';
import validate from './validate_hoja';

class Form extends Component {
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
            colaboradores_list,
            mi_cuenta,
            permisos_object,
        } = this.props;

        return (
            <MyFormTagModal
                onCancel={onCancel}
                onSubmit={handleSubmit((v) => {
                    if (!permisos_object.add_para_otros) {
                        if (mi_cuenta.colaborador) {
                            onSubmit({...v, colaborador: mi_cuenta.colaborador.id})
                        }
                    } else {
                        onSubmit(v)
                    }
                })}
                reset={reset}
                initialValues={initialValues}
                submitting={submitting}
                modal_open={modal_open}
                pristine={pristine}
                element_type={singular_name}
            >
                {
                    permisos_object.add_para_otros &&
                    <MyCombobox
                        data={_.map(_.pickBy(_.orderBy(colaboradores_list,['nombres'],['asc']), a => {
                            return (
                                a.autogestion_horas_trabajadas === false ||
                                a.usuario === mi_cuenta.id
                            )
                        }), e => {
                            return (
                                {
                                    id: e.id,
                                    nombre: `${e.nombres} ${e.apellidos}`
                                }
                            )
                        })}
                        className='col-12'
                        valuesField='id'
                        textField='nombre'
                        autoFocus={true}
                        name='colaborador'
                        placeholder='Colaborador'
                        filters='contains'
                    />
                }
                <MyDateTimePickerField
                    className='col-12 mb-5'
                    name='fecha'
                    nombre='Fecha'
                    dropUp={false}
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
        initialValues: item_seleccionado
    }
}

Form = reduxForm({
    form: "hojaTrabajoForm",
    validate,
    enableReinitialize: true
})(Form);

Form = (connect(mapPropsToState, null)(Form));

export default Form;