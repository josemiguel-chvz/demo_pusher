import { useEffect, useState } from "react";
import { Container, Row, Col } from "react-bootstrap";
import axios from "axios";
import Pusher from "pusher-js";
import ImageCard from "../components/ImageCard";


const BASE_URL = 'http://localhost:8000/api'

var pusher = new Pusher('cf43b99c5fa2fe4a6898', {
  encrypted: true,
  cluster: 'us2',
  authTransport: 'jsonp',
  authEndpoint: '/pusher/auth'
});

// var socketId = null;
// pusher.connection.bind('connected', function() {
// socketId = pusher.connection.socket_id;
// })


// DEV
// Pusher.logToConsole = true;

const Home = () => {
    const title = 'Feed';
    const [images, setImages] = useState([]);
    const [newImage, setNewImage] = useState({});

    const fetchImages = async () => {
      const response = await axios.get(BASE_URL+"/photo-feed/all");
      setImages(response.data)
    }

    const listenImages = () => {
      var channel = pusher.subscribe('photo_feed_channel');
      channel.bind("new_image", function (data) {
        setNewImage(data);
        fetchImages();
      });
    }

    useEffect(() => {
      fetchImages();
      listenImages();
      //eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return (
      <Container style={{display: 'flex', justifyContent: 'center', marginTop: '8px'}}>
        <Row className="border d-flex align-items-center justify-content-center mt-5">
          <Col>
            <h1 className="mb-2">
              {title}
            </h1>
            {images.map((image) => (
              <ImageCard key={image.id} image={image} />
            ))}
          </Col>
        </Row>
      </Container>
    )
}

export default Home;