import { createContext, useState } from "react";
import PropTypes from "prop-types";
import Api from "../services/api";
import _ from "lodash";
export const AuthContext = createContext();

export const AuthContextProvider = ({ children }) => {
  const auth = useAuthContext();
  return <AuthContext.Provider value={auth}>{children}</AuthContext.Provider>;
};

AuthContextProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

const useAuthContext = () => {
  const [user, setUser] = useState({});
  const [authed, setAuthed] = useState(false);
  const [loading, setLoading] = useState(true);
  const [passwordResetSent, setPasswordResetSent] = useState(false);
  const [passwordResetConfirmed, setPasswordResetConfirmed] = useState(false);
  const [errors, setErrors] = useState([]);
  const [socket, setWebsocket] = useState(null);
  const [socketMessages, setSocketMessages] = useState([]);

  const openSocketConnection = () => {
    let soc_url = "ws://192.168.45.18:8000/ws/";

    if (import.meta.env.VITE_APP_WS_URL) {
      soc_url = `${import.meta.env.VITE_APP_WS_URL}/ws/`;
    }

    const soc = new WebSocket(soc_url);

    setWebsocket(soc);

    soc.addEventListener("open", () => {
      soc.send(
        JSON.stringify({
          type: "Authorization",
          data: {
            token: localStorage.getItem("access_token"),
          },
        })
      );
    });

    soc.addEventListener("message", (e) => {
      setSocketMessages((prev) => [...prev, JSON.parse(e.data)]);
    });
  };

  const getUser = async () => {
    setLoading(true);
    return Api.me
      .get()
      .then((res) => {
        setUser(res.data);
        setAuthed(true);
        // openSocketConnection();
        setLoading(false);
        return res.data;
      })
      .catch(() => {
        localStorage.removeItem("access_token");
        setLoading(false);
        return false;
      });
  };

  const isAuthed = async () => {
    if (localStorage.getItem("access_token")) {
      await getUser();
      return true;
    } else {
      setLoading(false);
      return false;
    }
  };

  const signIn = async (data) => {
    return Api.signin.auth(data).then((res) => {
      localStorage.setItem("access_token", res.data.token);
      setErrors([]);
      return true;
    });
  };

  const signOut = async () => {
    setLoading(true);
    return Api.signOut.post().then(() => {
      localStorage.removeItem("access_token");
      // localStorage.removeItem("userCompany");
      setAuthed(false);
      setUser({});
      setLoading(false);
      if (socket) {
        socket.close();
      }
    });
  };

  const requestPasswordReset = (data) => {
    return Api.passwordReset
      .auth(data)
      .then((res) => {
        console.log(res.data);
        setErrors([]);
        setLoading(false);
        setPasswordResetSent(true);
      })
      .catch((e) => {
        setErrors([e.response.data.message]);
        setTimeout(() => {
          setErrors([]);
        }, 5000);
        console.log(e);
        setLoading(false);
      });
  };

  const ResetPasswordConfirm = (data) => {
    return Api.confirmPasswordReset
      .auth(data)
      .then(() => {
        setPasswordResetConfirmed(true);
        setLoading(false);
        setErrors([]);
      })
      .catch((e) => {
        setErrors([e.response.data.message]);
        setTimeout(() => {
          setErrors([]);
        }, 5000);
        setLoading(false);
      });
  };

  return {
    signIn,
    user,
    getUser,
    isAuthed,
    authed,
    signOut,
    loading,
    errors,
    setErrors,
    requestPasswordReset,
    passwordResetSent,
    ResetPasswordConfirm,
    passwordResetConfirmed,
  };
};
