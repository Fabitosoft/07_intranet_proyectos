import React, {Fragment} from 'react';
import MenuBase from '../../00_utilities/components/ui/menu/menu';
import Consultas from './consultas';
import HojasTrabajo from './hojasTrabajos';
import {Link} from 'react-router-dom'
import FontIcon from 'material-ui/FontIcon';

const iconStyles = {
    padding: 8,
};

const Menu = () => {
    return (
        <MenuBase>
            {mis_permisos => {
                return (
                    <Fragment>
                        <Consultas/>
                        <HojasTrabajo/>
                        <Link to='/app/proyectos/colaboradores/colaboradores/list'>
                            <FontIcon className="fas fa-user" style={iconStyles}/>
                        </Link>
                    </Fragment>
                )
            }}
        </MenuBase>
    )
};

export default Menu;