import React, { useState } from "react";
import axios from 'axios'
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import InputAdornment from "@material-ui/core/InputAdornment";
import Icon from "@material-ui/core/Icon";
// @material-ui/icons
import Email from "@material-ui/icons/Email";
import People from "@material-ui/icons/People";
// core components
import Header from "components/Header/Header.js";
import HeaderLinks from "components/Header/HeaderLinks.js";
import Footer from "components/Footer/Footer.js";
import GridContainer from "components/Grid/GridContainer.js";
import GridItem from "components/Grid/GridItem.js";
import Button from "components/CustomButtons/Button.js";
import Card from "components/Card/Card.js";
import CardBody from "components/Card/CardBody.js";
import CardHeader from "components/Card/CardHeader.js";
import CardFooter from "components/Card/CardFooter.js";
import CustomInput from "components/CustomInput/CustomInput.js";

import styles from "assets/jss/material-kit-react/views/loginPage.js";

import image from "assets/img/abundance.jpg";

const useStyles = makeStyles(styles);

export default function LoginPage(props) {

  // const handleSocialOnClick = (e) => {
  //   e.preventDefault()
  //   setUseSocialMessage(true)
  // }
  const [cardAnimaton, setCardAnimation] = React.useState("cardHidden");
  // const [socialMessage, setSocialMessage] = useState('Coming Soon!')
  // const [useSocialMessage, setUseSocialMessage] = useState(false)
  const [errorMessage, setErrorMessage] = useState('')
  const [errorMessageField, setErrorMessageField] = useState(null)
  const [useErrorMessage, setUseErrorMessage] = useState(false)
  const [usernameSignUp, setUsernameSignUp] = useState(null)
  const [usernameLogin, setUsernameLogin] = useState(null)
  const [email, setEmail] = useState(null)
  const [passwordSignUp, setPasswordSignUp] = useState(null)
  const [passwordSignUp2, setPasswordSignUp2] = useState(null)
  const [passwordLogin, setPasswordLogin] = useState(null)
  const handleUsernameSignUpChange = (e) => {
    setUsernameSignUp(e.target.value)
  }
  const handleUsernameLoginChange = (e) => {
    setUsernameLogin(e.target.value)
  }
  const handlePasswordSignUpChange = (e) => {
    setPasswordSignUp(e.target.value)
  }
  const handlePasswordSignUpChange2 = (e) => {
    setPasswordSignUp2(e.target.value)
  }
  const handlePasswordLoginChange = (e) => {
    setPasswordLogin(e.target.value)
  }
  const handleEmailChange = (e) => {
    setEmail(e.target.value)
  }
  setTimeout(function() {
    setCardAnimation("");
  }, 700);
  const classes = useStyles();
  const { ...rest } = props;
  const loginPost = () => {
    axios.post(
      '/rest-auth/login/',
      {
        username: usernameLogin,
        password: passwordLogin
      }
    )
    .then((response) => {
      console.log(response)
    })
    .catch((error) => {
      console.log(error)
    })
  }
  const signUpPost = () => {
    axios.post(
      '/rest-auth/registration/',
      {
        username: usernameSignUp,
        email: email,
        password1: passwordSignUp,
        password2: passwordSignUp2,
      }
    )
    .then((response) => {
      console.log(response)
    })
    .catch((error) => {
      console.log(error)
    })
  }
  return (
    <div>
      <Header
        absolute
        color="transparent"
        brand="👑 Queens Cake N Bake 🎂"
        rightLinks={<HeaderLinks />}
        {...rest}
      />
      <div
        className={classes.pageHeader}
        style={{
          backgroundImage: "url(" + image + ")",
          backgroundSize: "cover",
          backgroundPosition: "top center"
        }}
      >
        <div className={classes.container}>
          <GridContainer justify="center">
            <GridItem xs={12} sm={12} md={4}>
              <Card className={classes[cardAnimaton]}>
                <form className={classes.form}>
                  <CardHeader color="primary" className={classes.cardHeader}>
                    <h4>Login</h4>
                    <CustomInput
                      labelText="Username..."
                      id="usernameLogin"
                      formControlProps={{
                        fullWidth: true
                      }}
                      inputProps={{
                        type: "text",
                        endAdornment: (
                          <InputAdornment position="end">
                            <People className={classes.inputIconsColor} />
                          </InputAdornment>
                        )
                      }}
                      onChange={handleUsernameLoginChange}
                    />
                    <CustomInput
                      labelText="Password"
                      id="pass"
                      formControlProps={{
                        fullWidth: true
                      }}
                      inputProps={{
                        type: "passwordLogin",
                        endAdornment: (
                          <InputAdornment position="end">
                            <Icon className={classes.inputIconsColor}>
                              lock_outline
                            </Icon>
                          </InputAdornment>
                        ),
                        autoComplete: "off"
                      }}
                      onChange={handlePasswordLoginChange}
                    />
                    <Button
                      simple
                      color='secondary'
                      size='lg'
                      onClick={loginPost}
                    >
                      Login
                    </Button>
                    {/* <div className={classes.socialLine}>
                      <Button
                        justIcon
                        href="#pablo"
                        target="_blank"
                        color="transparent"
                        onClick={e => e.preventDefault()}
                      >
                        <i className={"fab fa-twitter"} />
                      </Button>
                      <Button
                        justIcon
                        href="#pablo"
                        target="_blank"
                        color="transparent"
                        onClick={e => e.preventDefault()}
                      >
                        <i className={"fab fa-facebook"} />
                      </Button>
                      <Button
                        justIcon
                        href="#pablo"
                        target="_blank"
                        color="transparent"
                        onClick={e => e.preventDefault()}
                      >
                        <i className={"fab fa-google-plus-g"} />
                      </Button>
                    </div> */}
                  </CardHeader>
                  <p className={classes.divider}>Or create an account</p>
                  <CardBody>
                    <CustomInput
                      labelText="Username..."
                      id="usernameSignUp"
                      formControlProps={{
                        fullWidth: true
                      }}
                      inputProps={{
                        type: "text",
                        endAdornment: (
                          <InputAdornment position="end">
                            <People className={classes.inputIconsColor} />
                          </InputAdornment>
                        )
                      }}
                      onChange={handleUsernameSignUpChange}
                    />
                    <CustomInput
                      labelText="Email..."
                      id="email"
                      formControlProps={{
                        fullWidth: true
                      }}
                      inputProps={{
                        type: "email",
                        endAdornment: (
                          <InputAdornment position="end">
                            <Email className={classes.inputIconsColor} />
                          </InputAdornment>
                        )
                      }}
                      onChange={handleEmailChange}
                    />
                    <CustomInput
                      labelText="Password"
                      id="passwordSignUp"
                      formControlProps={{
                        fullWidth: true
                      }}
                      inputProps={{
                        type: "password",
                        endAdornment: (
                          <InputAdornment position="end">
                            <Icon className={classes.inputIconsColor}>
                              lock_outline
                            </Icon>
                          </InputAdornment>
                        ),
                        autoComplete: "off"
                      }}
                      onChange={handlePasswordSignUpChange}
                    />
                    <CustomInput
                      labelText="Password"
                      id="passwordSignUp2"
                      formControlProps={{
                        fullWidth: true
                      }}
                      inputProps={{
                        type: "password",
                        endAdornment: (
                          <InputAdornment position="end">
                            <Icon className={classes.inputIconsColor}>
                              lock_outline
                            </Icon>
                          </InputAdornment>
                        ),
                        autoComplete: "off"
                      }}
                      onChange={handlePasswordSignUpChange2}
                    />
                  </CardBody>
                  <CardFooter className={classes.cardFooter}>
                    <Button
                      simple
                      color='primary'
                      size='lg'
                      onClick={signUpPost}
                    >
                      Get Started
                    </Button>
                  </CardFooter>
                </form>
              </Card>
            </GridItem>
          </GridContainer>
        </div>
        <Footer whiteFont />
      </div>
    </div>
  );
}
