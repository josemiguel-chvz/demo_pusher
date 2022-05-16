import './App.css';
import { Container } from 'react-bootstrap';
import { Routes, Route } from "react-router-dom";
import Layout from "./layouts/Layout";
import Home from "./pages/Home";
import UploadImage from "./pages/UploadImage";


const App = () => {
  return (
      <Layout>
        <Container>
          <Routes>
            <Route path="/" element={<Home />} exact />
            <Route path="/upload" element={<UploadImage />} exact/>
          </Routes>
        </Container>
      </Layout>
  );
}

export default App;
