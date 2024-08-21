import { Route, Routes } from "react-router-dom";
import Navbar from "../components/navbar";
import Parlays from "./parlays";

const Home = () => {
  return (
    <>
      <div className="w-screen">
        <Navbar />
      </div>

      <Routes>
        <Route path="/" element={<Parlays />} />
      </Routes>
    </>
  );
};

export default Home;
