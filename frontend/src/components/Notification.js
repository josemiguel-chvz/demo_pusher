import { Toast, ToastContainer } from "react-bootstrap";

const Notification = ({show, handleNotificationStatus, notification}) => {
  return (
    <ToastContainer className="p-3 mt-5" position='top-end' style={{zIndex: 1}}>
      <Toast
        show={show}
        onClose={() => handleNotificationStatus(!show)}
        delay={15000} autohide
        bg="light"
      >
        <Toast.Header>
          <img
            src="holder.js/20x20?text=%20"
            className="rounded me-2"
            alt=""
          />
          <strong className="me-auto">{notification.title}</strong>
          <small>Ahora</small>
        </Toast.Header>
        <Toast.Body>
          {notification.username} ha subido {notification.description}
        </Toast.Body>
      </Toast>
    </ToastContainer>
  )
}

export default Notification;
