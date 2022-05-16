import Menu from "../components/Menu";
// import footer from "../components/footer";
import Notification from "../components/Notification";
import React, { useState, useEffect } from "react";
import Pusher from "pusher-js";



// const BASE_URL = 'http://localhost:8000/api'

var pusher = new Pusher('cf43b99c5fa2fe4a6898', {
  encrypted: true,
  cluster: 'us2',
  authTransport: 'jsonp',
  authEndpoint: '/pusher/auth'
});

Pusher.logToConsole = true;


const Layout = ({children}) => {
    const [show, setShow] = useState(false);
    const [newNotification, setNewNotification] = useState({});

    const handleNotificationStatus = (status) => {
      setShow(status);
    }

    const listenNotifications = () => {
      var channel = pusher.subscribe('notification_channel');
      channel.bind("new_notification", function (data) {
        setShow(true);
        setNewNotification(data);
      });
    }

    useEffect(() => {
      listenNotifications();
      //eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return (
        <>
          <Menu  />
          <Notification
            show={show}
            notification={newNotification}
            handleNotificationStatus={handleNotificationStatus}
          />
          <main>{children}</main>
        </>
    );
};

export default Layout;