import React, {Component} from 'react';
import {MyDialogButtonDelete} from '../../../../00_utilities/components/ui/dialog';
import {fechaFormatoUno} from "../../../../00_utilities/common";

const ListaArchivoItem = (props) => <tr>
    <td style={{padding: '4px'}}>{props.item.nombre_archivo}</td>
    <td style={{padding: '4px'}}>{fechaFormatoUno(props.item.created)}</td>
    <td style={{padding: '4px'}}>{props.item.creado_por_username}</td>
    <td style={{padding: '2px'}} className='text-center'><a href={props.item.archivo_url}>
        <i className='fas fa-download fa-2x puntero'></i></a>
    </td>
    <td style={{padding: '2px'}} className='text-center'>
        <i className='fas fa-edit fa-2x puntero' onClick={() => props.onSelectElemento(props.item)}></i>
    </td>
    <td style={{padding: '2px'}} className='text-center'>
        <MyDialogButtonDelete
            onDelete={() => {
                props.onDeleteArchivo(props.item.id)
            }}
            element_name={props.item.nombre_archivo}
            element_type='Archivo'
        />
    </td>
</tr>;

export default class ListaArchivosList extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        const {lista, onDeleteArchivo, onSelectElemento} = this.props;
        return (
            <table className='table table-responsive table-striped' style={{fontSize: '11px'}}>
                <thead>
                <tr>
                    <th style={{padding: '2px'}}>Nombre</th>
                    <th style={{padding: '2px'}}>Fecha</th>
                    <th style={{padding: '2px'}}>Usuario</th>
                    <th style={{padding: '2px'}}>Link</th>
                    <th style={{padding: '2px'}}>Editar</th>
                    <th style={{padding: '2px'}}>Eliminar</th>
                </tr>
                </thead>
                <tbody>
                {_.map(lista, e => <ListaArchivoItem item={e} key={e.id} onDeleteArchivo={onDeleteArchivo}
                                                     onSelectElemento={onSelectElemento}/>)}
                </tbody>
            </table>
        )
    }
};