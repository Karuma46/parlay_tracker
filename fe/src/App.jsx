import { Route, Routes, useNavigate } from "react-router-dom";
import Login from "./auth/login";
import { useContext, useEffect } from "react";
import { AuthContext, AuthContextProvider } from "./auth/authContext";
import Home from "./home";

function App() {
  const { isAuthed, authed } = useContext(AuthContext);

  const navigate = useNavigate();

  useEffect(() => {
    isAuthed();
  }, []);

  useEffect(() => {
    if (authed) {
      navigate("/");
    } else {
      navigate("/login");
    }
  }, [authed]);

  return (
    <>
      <AuthContextProvider>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route exact path="/login" element={<Login />} />
        </Routes>
      </AuthContextProvider>
    </>
  );
}

export default App;
