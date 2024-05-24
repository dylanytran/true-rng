import React, { useState, useEffect } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import "../styles/Navbar.css";

function Navbar() {
    return (
        <div className="navbar">
            <div className="links">
                <NavLink to="/" exact activeClassName="active">Home</NavLink>
                <NavLink to="/about" activeClassName="active">About</NavLink>
            </div>
        </div>
    );
}

export default Navbar;