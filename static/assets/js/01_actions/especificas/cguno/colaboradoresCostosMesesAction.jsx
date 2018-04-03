import {
    CREATE_COLABORADOR_COSTO_MES,
    DELETE_COLABORADOR_COSTO_MES,
    FETCH_COLABORADORES_COSTOS_MESES,
    FETCH_COLABORADOR_COSTO_MES,
    CLEAR_COLABORADORES_COSTOS_MESES,
    UPDATE_COLABORADOR_COSTO_MES,
} from '../../00_types';
import {
    fetchList,
    updateObject,
    fetchObject,
    deleteObject,
    createObject,
    fetchListWithParameter
} from '../../00_general_fuctions'

const current_url_api = 'colaboradores_costo_nomina';
export const createColaboradorCostoMes = (values, callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: CREATE_COLABORADOR_COSTO_MES, payload: response})
        };
        createObject(current_url_api, values, dispatches, callback, callback_error)
    }
};
export const deleteColaboradorCostoMes = (id, callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: DELETE_COLABORADOR_COSTO_MES, payload: id})
        };
        deleteObject(current_url_api, id, dispatches, callback, callback_error)
    }
};
export const fetchColaboradoresCostosMeses = (callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: FETCH_COLABORADORES_COSTOS_MESES, payload: response})
        };
        fetchList(current_url_api, dispatches, callback, callback_error);
    }
};
export const fetchColaboradoresCostosMesesxFechas = (fecha_inicial, fecha_final, callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: FETCH_COLABORADORES_COSTOS_MESES, payload: response})
        };
        fetchListWithParameter(`${current_url_api}/listar_x_fechas/?fecha_inicial=${fecha_inicial}&fecha_final=${fecha_final}`, dispatches, callback, callback_error);
    }
};
export const fetchColaboradorCostoMes = (id, callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: FETCH_COLABORADOR_COSTO_MES, payload: response})
        };
        fetchObject(current_url_api, id, dispatches, callback, callback_error);
    }
};
export const clearColaboradoresCostosMeses = () => {
    return (dispatch) => {
        dispatch({type: CLEAR_COLABORADORES_COSTOS_MESES});

    }
};
export const updateColaboradorCostoMes = (id, values, callback = null, callback_error = null) => {
    return (dispatch) => {
        const dispatches = (response) => {
            dispatch({type: UPDATE_COLABORADOR_COSTO_MES, payload: response})
        };
        updateObject(current_url_api, id, values, dispatches, callback, callback_error)
    }
};