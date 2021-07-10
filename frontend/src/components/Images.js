import React, { useState, useEffect } from "react";
import { Jumbotron, Button, Image } from 'react-bootstrap';
import UserService from "../services/user.service";


const Images = () => {
    const [content, setContent] = useState("");
    const [lastItem, setLastItem] = useState("");

  useEffect(() => {
    UserService.getPublicContent("product?expand=image").then(
      (response) => {
        setContent(response.data);
        setLastItem(response.data[0]);
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
        {lastItem.name} {lastItem.image}
    </div>
    ); 
};

export default Images;