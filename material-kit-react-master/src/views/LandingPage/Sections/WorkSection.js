import React, { useState, useEffect } from "react";
import axios from 'axios'
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";

// @material-ui/icons

// core components
import GridContainer from "components/Grid/GridContainer.js";
import GridItem from "components/Grid/GridItem.js";
import CustomInput from "components/CustomInput/CustomInput.js";
import Button from "components/CustomButtons/Button.js";

import styles from "assets/jss/material-kit-react/views/landingPageSections/workStyle.js";

const useStyles = makeStyles(styles);

export default function WorkSection() {

  const [fullName, setFullName] = useState('')
  const [email, setEmail] = useState('')
  const [message, setMessage] = useState('')

  const validateFullName = (name) => {
    let regName = /^[a-zA-Z]+ [a-zA-Z]+$/
    return regName.test(name) ?
    true :
    false
  }
  const validateEmail = (email) => {
    // let regEmail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
    let regEmail = /^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/
    return regEmail.test() ?
    true :
    false
  }
  const validateMessage = (message) => {
    let regMessage = /[^a-zA-Z0-9\-\/]/
    return regMessage.test() ?
    true :
    false        
  }
  const fullNameHandler = (e) => {
    setFullName(e.target.value)
  }
  const emailHandler = (e) => {
    setEmail(e.target.value)
  }
  const isEmailValid = (email) => {
    return validateEmail(email) ?
    true :
    false
  }
  const isFullNameValid = (fullname) => {
    return validateFullName(fullname) ?
    true :
    false
  }
  const messageHandler = (e) => {
    setMessage(e.target.value)
  }
  const isMessageValid = (message) => {
    return
  }
  const post = () => {
    axios.post(
      '/contact/',
      {
        full_name: fullName,
        email: email,
        user_message: message,
      }
    )
      .then(
        (response) => {
          console.log(response)
        }
      )
      .catch(
        (error) => {
          console.log(error)
        }
      )
  }
  const classes = useStyles();
  return (
    <div className={classes.section}>
      <GridContainer justify="center">
        <GridItem cs={12} sm={12} md={8}>
          <h2 className={classes.title}>Work with us</h2>
          <h4 className={classes.description}>
            Divide details about your product or agency work into parts. Write a
            few lines about each one and contact us about any further
            collaboration. We will responde get back to you in a couple of
            hours.
          </h4>
          <form>
            <GridContainer>
              <GridItem xs={12} sm={12} md={6}>
                <CustomInput
                  labelText="Your Name"
                  id="name"
                  formControlProps={{
                    fullWidth: true
                  }}
                  onChange={fullNameHandler}
                  // error={isFullNameValid(fullName) ? true : false}
                  // success={isFullNameValid(fullName) ? true : false}
                />
              </GridItem>
              <GridItem xs={12} sm={12} md={6}>
                <CustomInput
                  labelText="Your Email"
                  id="email"
                  formControlProps={{
                    fullWidth: true
                  }}
                  onChange={emailHandler}
                  // error={isEmailValid(email) ? true : false}
                  // success={isEmailValid(email) ? true : false}
                />
              </GridItem>
              <CustomInput
                labelText="Your Message"
                id="message"
                formControlProps={{
                  fullWidth: true,
                  className: classes.textArea
                }}
                inputProps={{
                  multiline: true,
                  rows: 5
                }}
                onChange={messageHandler}
              />
              <GridItem xs={12} sm={12} md={4}>
                <Button
                  color='primary'
                  onClick={post}
                >
                  Send Message
                </Button>
              </GridItem>
            </GridContainer>
          </form>
        </GridItem>
      </GridContainer>
    </div>
  );
}
