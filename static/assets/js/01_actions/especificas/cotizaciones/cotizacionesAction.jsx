import {COTIZACION_TYPES as TYPES} from '../../00_types';
import {
    fetchList,
    updateObject,
    fetchObject,
    deleteObject,
    createObject,
    callApiMethodWithParametersPDF,
    fetchListWithParameter
} from '../../00_general_fuctions'

const current_url_api = 'cotizaciones';
export const createCotizacion = (values, callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: TYPES.create, payload: response})
        };
        createObject(current_url_api, values, dispatches, callback, callback_error)
    }
};
export const deleteCotizacion = (id, callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: TYPES.delete, payload: id})
        };
        deleteObject(current_url_api, id, dispatches, callback, callback_error)
    }
};
export const fetchCotizaciones = (callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: TYPES.fetch_all, payload: response})
        };
        fetchList(current_url_api, dispatches, callback, callback_error);
    }
};
export const fetchCotizacionesAgendadas = (callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: TYPES.fetch_all, payload: response})
        };
        fetchList(`${current_url_api}/listar_cotizaciones_agendadas`, dispatches, callback, callback_error);
    }
};
export const fetchCotizacionesPidiendoCarpeta = (callback = null, callback_error = null) => {
    return function (dispatch) {
        const FULL_URL = `${current_url_api}/listar_cotizacion_abrir_carpeta`;
        const dispatches = (response) => {
            dispatch({type: TYPES.fetch_all, payload: response})
        };
        fetchList(FULL_URL, dispatches, callback, callback_error);
    }
};
export const fetchCotizacionesTuberiaVentas = (callback = null, callback_error = null) => {
    return function (dispatch) {
        const FULL_URL = `${current_url_api}/listar_cotizaciones_tuberia_ventas`;
        const dispatches = (response) => {
            dispatch({type: TYPES.fetch_all, payload: response})
        };
        fetchList(FULL_URL, dispatches, callback, callback_error);
    }
};
export const fetchCotizacionesTuberiaVentasResumen = (ano = null, trimestre = null, callback = null, callback_error = null) => {
    return function (dispatch) {
        const dispatches = (response) => {
            dispatch({type: TYPES.fetch_all, payload: response})
        };
        if (ano && trimestre) {
            const FULL_URL = `${current_url_api}/cotizaciones_resumen_tuberia_ventas/?ano=${ano}&trimestre=${trimestre}`;
            fetchListWithParameter(FULL_URL, dispatches, callback, callback_error);
        } else {
            const FULL_URL = `${current_url_api}/cotizaciones_resumen_tuberia_ventas`;
            fetchList(FULL_URL, dispatches, callback, callback_error);
        }
    }
};
export const fetchCotizacion = (id, callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: TYPES.fetch, payload: response})
        };
        fetchObject(current_url_api, id, dispatches, callback, callback_error);
    }
};
export const clearCotizaciones = () => {
    return (dispatch) => {
        dispatch({type: TYPES.clear});

    }
};
export const updateCotizacion = (id, values, callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: TYPES.update, payload: response})
        };
        updateObject(current_url_api, id, values, dispatches, callback, callback_error)
    }
};
export const uploadArchivoCotizacion = (id, values, callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: TYPES.upload, payload: response})
        };
        callApiMethodWithParametersPDF(current_url_api, id, 'upload_archivo', values, dispatches, callback, callback_error)
    }
};