import React, {Component} from 'react';
import CambiarPinForm from './forms/cambiar_pin_form'
import CambiarContrasenaForm from './forms/cambiar_contrasena_form'
import {connect} from "react-redux";
import * as actions from "../../../../01_actions/01_index";
import Typography from '@material-ui/core/Typography';

class Seguridad extends Component {
    constructor(props) {
        super(props);
        this.onCambiarPin = this.onCambiarPin.bind(this);
        this.onCambiarPassword = this.onCambiarPassword.bind(this);
    }

    onCambiarPin(values, callback) {
        const {cambiarPinUsuario} = this.props;
        const mi_cuenta = JSON.parse(localStorage.getItem('mi_cuenta'));
        cambiarPinUsuario(mi_cuenta.id, values.pin, values.password, {callback});
    }

    onCambiarPassword(values, callback) {
        const {
            cambiarContrasenaUsuario
        } = this.props;
        const mi_cuenta = JSON.parse(localStorage.getItem('mi_cuenta'));

        cambiarContrasenaUsuario(
            mi_cuenta.id,
            values.password_old,
            values.password,
            values.password_2,
            {callback}
        )
    }

    render() {
        const mi_cuenta = JSON.parse(localStorage.getItem('mi_cuenta'));
        return (
            <div className="row">
                {
                    mi_cuenta.tercero &&
                    <div className="col-12">
                        <Typography variant="h4" gutterBottom color="primary">
                            Cambiar Pin
                        </Typography>
                        <CambiarPinForm onSubmit={this.onCambiarPin}/>
                    </div>
                }
                <div className="col-12 mt-3">
                    <Typography variant="h4" gutterBottom color="primary">
                        Cambiar Contraseña
                    </Typography>
                    <CambiarContrasenaForm onSubmit={this.onCambiarPassword}/>
                </div>
            </div>
        )
    }
}

function mapPropsToState(state, ownProps) {
    return {
        auth: state.auth,
    }
}

export default connect(mapPropsToState, actions)(Seguridad)