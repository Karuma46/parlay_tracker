import { Route, Routes, useNavigate } from "react-router-dom";
import Login from "./auth/login";
import { useContext, useEffect, useState } from "react";
import { AuthContext, AuthContextProvider } from "./auth/authContext";

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
          <Route path="/login" element={<Login />} />
        </Routes>
      </AuthContextProvider>
    </>
  );
}

export default App;
