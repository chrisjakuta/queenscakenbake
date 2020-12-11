import React, { Component } from 'react'

// nodejs library that concatenates classes
import classNames from "classnames"
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles"

// @material-ui/icons

// core components
import Header from "components/Header/Header.js"
import Footer from "components/Footer/Footer.js"
import GridContainer from "components/Grid/GridContainer.js"
import GridItem from "components/Grid/GridItem.js"
import Button from "components/CustomButtons/Button.js"
import HeaderLinks from "components/Header/HeaderLinks.js"
import Parallax from "components/Parallax/Parallax.js"

import styles from "assets/jss/material-kit-react/views/landingPage.js"

const dashboardRoutes = []

const useStyles = makeStyles(styles)

export default function ConfectionaryDetail(props) {

    const classes = useStyles()
    const { ...rest } = props

    return (
        <div>
            <Header
                color='transparent'
                routes={dashboardRoutes}
                brand="👑 Queens Cake N Bake 🎂"
                rightLinks={<HeaderLinks />}
                fixed
                changeColorOnScroll={{
                    height: 400,
                    color: "white"
                }}
                {...rest}
            />
        </div>
    )
}
