import { Card } from "react-bootstrap";

const ImageCard = ({image}) => {
  const image_url = "http://localhost:8000" + image.image;
  return (
    <Card style={{ width: '25rem', marginBottom: '25px'}}>
      <Card.Img variant="top" src={image_url} />
      <Card.Body>
          <Card.Title>{image.description}</Card.Title>
      </Card.Body>
    </Card>
  )
}

export default ImageCard;