import React from "react";
import ReactDOM from "react-dom";
import { createBrowserHistory } from "history";
import { Router, Route, Switch, Redirect } from "react-router-dom";

import "assets/scss/material-kit-react.scss?v=1.9.0";

// pages for this product
import Components from "views/Components/Components.js";
import LandingPage from "views/LandingPage/LandingPage.js";
import ProfilePage from "views/ProfilePage/ProfilePage.js";
import LoginPage from "views/LoginPage/LoginPage.js";
import ConfectioneryDetail from 'views/confectionery/ConfectioneryDetail'

var hist = createBrowserHistory();

ReactDOM.render(
  <Router history={hist}>
    <Switch>
      <Route path="/home" component={LandingPage} />
      <Route path="/login" component={LoginPage} />
      {/* <Route path="/home" component={Components} /> */}
      <Route path="/confectionery" component={ProfilePage} />
      <Route
        path='/confectionery/:type'
        component={ConfectioneryDetail}
      />
      <Route
        path='/confectionery/:type/:name'
        component={ConfectioneryDetail}
      />
      <Redirect
        to='/home'
        from='/'
      />
    </Switch>
  </Router>,
  document.getElementById("root")
);
