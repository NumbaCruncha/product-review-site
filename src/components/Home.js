import React, { useState, useEffect } from "react";
import { Jumbotron, Button, Image } from 'react-bootstrap';
import UserService from "../services/user.service";


const Home = () => {
    const [content, setContent] = useState("");
    const [lastItem, setLastItem] = useState("");

  useEffect(() => {
    UserService.getPublicContent("product").then(
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
    <Jumbotron>
  <h1>{ lastItem.name }</h1>
  <h3>Index { lastItem.pk }</h3>
  <h5>Reviewed by {lastItem.user} on { lastItem.created }</h5>
  
  <p>
      <Image></Image>
    { lastItem.content }
  </p>
  <p>
    <Button variant="primary">Learn more</Button>
  </p>
</Jumbotron>
</div>
  );
};
export default Home;