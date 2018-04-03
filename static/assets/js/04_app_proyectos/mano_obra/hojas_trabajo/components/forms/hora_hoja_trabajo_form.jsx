import React, {Component, Fragment} from 'react';
import {reduxForm} from 'redux-form';
import {
    MyCombobox,
    MyTextFieldSimple,
} from '../../../../../00_utilities/components/ui/forms/fields';
import {connect} from "react-redux";
import {MyFormTagModal} from '../../../../../00_utilities/components/ui/forms/MyFormTagModal';
import validate from './validate_horas';

class Form extends Component {
    constructor(props) {
        super(props);
        this.state = ({
            proyecto: null
        });
    }

    componentDidMount() {
        const {initialValues, proyectos_list, mi_cuenta} = this.props;
        const autogestion_horas_trabajadas = !!(
            mi_cuenta.colaborador &&
            mi_cuenta.colaborador.autogestion_horas_trabajadas
        );

        let proyectos_list_array = proyectos_list;

        console.log(proyectos_list_array)
        if (autogestion_horas_trabajadas) {
            proyectos_list_array = this.getListaAutorizada();
        }

        console.log(proyectos_list_array)

        if (initialValues) {
            const {proyecto} = initialValues;
            this.setState({proyecto: proyectos_list_array[proyecto]});
        }
    }

    getListaAutorizada() {
        const {
            proyectos_list,
            mi_cuenta,
            initialValues,
        } = this.props;
        let literales_autorizados = mi_cuenta.colaborador.literales_autorizados;

        if (initialValues) {
            literales_autorizados = [...literales_autorizados, initialValues.literal]
        }

        let proyectos_list_array = _.map(proyectos_list, e => {
            return ({
                ...e,
                mis_literales: e.mis_literales.filter(e => literales_autorizados.includes(e.id))
            })
        });
        proyectos_list_array = _.pickBy(proyectos_list_array, e => e.mis_literales.length > 0);
        proyectos_list_array = _.mapKeys(proyectos_list_array, 'id');
        return proyectos_list_array;
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
            proyectos_list,
            object,
            mi_cuenta,
            hoja_trabajo,
        } = this.props;
        const {proyecto} = this.state;

        const autogestion_horas_trabajadas = !!(
            mi_cuenta.colaborador &&
            mi_cuenta.colaborador.autogestion_horas_trabajadas
        );

        let verificado = false;

        if (initialValues) {
            verificado = initialValues.verificado;
        }

        let proyectos_list_array = _.map(proyectos_list, e => e);
        if (autogestion_horas_trabajadas) {
            proyectos_list_array = _.map(this.getListaAutorizada(), e => e);
        }

        return (
            <MyFormTagModal
                onCancel={onCancel}
                onSubmit={handleSubmit((e) => {
                    const verificado = !autogestion_horas_trabajadas;
                    const autogestionada = autogestion_horas_trabajadas;
                    const cantidad_minutos = (Number(e.horas * 60) + Number(e.minutos));
                    onSubmit({...e, hoja: object.id, cantidad_minutos, autogestionada, verificado});
                })}
                reset={reset}
                initialValues={initialValues}
                submitting={submitting}
                modal_open={modal_open}
                pristine={pristine}
                element_type={singular_name}
            >
                {
                    !verificado ?
                        <Fragment>
                            <MyCombobox
                                data={proyectos_list_array}
                                className='col-12'
                                valuesField='id'
                                textField='id_proyecto'
                                autoFocus={true}
                                onSelect={(e) => {
                                    this.setState({proyecto: e});
                                }}
                                name='proyecto'
                                onChange={v => v.id}
                                placeholder='Proyecto'
                                caseSensitive={false}
                                minLength={3}
                                filter='contains'
                            />
                            {
                                proyecto &&
                                proyecto.mis_literales &&
                                <MyCombobox
                                    data={_.map(_.pickBy(proyecto.mis_literales, li => {
                                        return (
                                            !_.map(hoja_trabajo.mis_horas_trabajadas, e => e.literal).includes(li.id)
                                            || (initialValues && li.id === initialValues.literal)
                                        )
                                    }), e => {
                                        return ({
                                            id: e.id,
                                            descripcion: `${e.id_literal} - ${e.descripcion}`
                                        })
                                    })}
                                    className='col-12'
                                    valuesField='id'
                                    textField='descripcion'
                                    autoFocus={true}
                                    name='literal'
                                    placeholder='Literales'
                                    caseSensitive={false}
                                    minLength={3}
                                    filter='contains'
                                />
                            }
                            {
                                <div className='col-12'>
                                    <div className="row">
                                        <MyTextFieldSimple disabled={verificado} name='horas' nombre='Horas'
                                                           className='col-6'/>
                                        <MyTextFieldSimple disabled={verificado} name='minutos' nombre='Minutos'
                                                           className='col-6'/>
                                    </div>
                                </div>
                            }

                            <MyTextFieldSimple
                                name='descripcion_tarea'
                                nombre='Descripción'
                                rows={5}
                                multiLine={true}
                                className='col-12'
                                disabled={!autogestion_horas_trabajadas || verificado}
                            />
                            <div style={{height: '300px'}}>

                            </div>
                        </Fragment> :
                        <span>Esta verificado, no se puede cambiar</span>
                }
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