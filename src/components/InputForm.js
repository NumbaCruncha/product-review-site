import React, { useState, useEffect } from "react";
import { Form, Button, Image } from 'react-bootstrap';
import UserService from "../services/user.service";

const InputForm = () => {
    
    const [name, setName] = useState("");
    const [content, setContent] = useState("");

  useEffect(() => {
    UserService.postInputForm("product").then(
      (response) => {
        setContent(response.data);
 
      },
      (error) => {
        const _content =
          (error.response && error.response.data) ||
          error.message ||
          error.toString();

        setContent(_content);
      }
    );
  }, []);

return (
    <div>
        <Form>
            <Form.Group controlId="name">
                <Form.Label>Model</Form.Label>
                <Form.Control type="text" placeholder="Enter the model."/>
            </Form.Group>
      
            <Form.Group controlId="content">
                <Form.Label>Description</Form.Label>
                <Form.Control type="text" placeholder="Enter the review here."/>
            </Form.Group>
            <div className="mb-3">
                <Button variant="primary" type="submit" >
                    Submit
                </Button>
            </div>
        </Form>
    </div>
    ); 
};

export default InputForm;