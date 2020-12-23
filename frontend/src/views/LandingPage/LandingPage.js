import React, { useState, useEffect } from "react";
import axios from 'axios'
// nodejs library that concatenates classes
import classNames from "classnames";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";

// @material-ui/icons

// core components
import Header from "components/Header/Header.js";
import Footer from "components/Footer/Footer.js";
import GridContainer from "components/Grid/GridContainer.js";
import GridItem from "components/Grid/GridItem.js";
import Button from "components/CustomButtons/Button.js";
import HeaderLinks from "components/Header/HeaderLinks.js";
import Parallax from "components/Parallax/Parallax.js";

import styles from "assets/jss/material-kit-react/views/landingPage.js";

// Sections for this page
import ProductSection from "./Sections/ProductSection.js";
import TeamSection from "./Sections/TeamSection.js";
import WorkSection from "./Sections/WorkSection.js";
// backend constants
// import {
//   allProducts,
//   allProxyProducts,
//   individualProxyItem,
// } from '../../backendConstants'

const dashboardRoutes = [];

const useStyles = makeStyles(styles);

export default function LandingPage(props) {
  const [data, setData] = useState(null)
  const classes = useStyles();

  useEffect(() => {
    if (!data) {
      axios.get('/landing')
        .then((response) => {
          const { ...data } = response.data
          setData(data)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  })
  const { ...rest } = props;
  return (
    <div>
      <Header
        color="transparent"
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
      <Parallax filter image={require("assets/img/abundance.jpg")}>
        <div className={classes.container}>
          <GridContainer>
            <GridItem xs={12} sm={12} md={6}>
              {
                data ?
                <h1 className={classes.title}>{data.header_text}</h1> :
                <h1 className={classes.title}>Your Sweet Tooth, Our Passion.</h1>
              }
              {
                data ?
                <h4>{data.landing_page_text}</h4> :
                <h4>
                Every landing page needs a small description after the big bold
                title, that{"'"}s why we added this text here. Add here all the
                information that can make you or your product create the first
                impression.
              </h4>
              }
              <br />
              <Button
                color="danger"
                size="lg"
                href="#"
                target="_blank"
                rel="noopener noreferrer"
              >
                <i className="fas fa-play" />
                Watch video
              </Button>
            </GridItem>
          </GridContainer>
        </div>
      </Parallax>
      <div className={classNames(classes.main, classes.mainRaised)}>
        <div className={classes.container}>
          <ProductSection
            productSectionHeaderText={ data && data.product_section_header_text}
            productSectionText={ data && data.product_section_text}
          />
          <TeamSection />
          <WorkSection />
        </div>
      </div>
      <Footer />
    </div>
  );
}
