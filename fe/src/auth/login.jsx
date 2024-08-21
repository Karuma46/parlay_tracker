import { faLock } from "@fortawesome/free-solid-svg-icons";
import { TextInput } from "../components/inputs";
import { faUser } from "@fortawesome/free-regular-svg-icons";
import { useContext, useState } from "react";
import { AuthContext } from "./authContext";

const Login = () => {
  const { signIn, getUser } = useContext(AuthContext);
  const [creds, setCreds] = useState({
    username: "s.karuma",
    password: "karuma",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (await signIn(creds)) {
      getUser();
    }
  };

  return (
    <>
      <div className="w-screen h-screen flex justify-center items-center">
        <div className="w-[500px] border border-primary/30 rounded-lg p-8">
          <div>
            <p className="text-3xl font-light">Sign In</p>
          </div>
          <div className="divider"></div>
          <div className="w-full">
            <form
              className="w-full flex flex-col gap-8"
              onSubmit={handleSubmit}>
              <TextInput
                placeholder="Username"
                icon={faUser}
                value={creds.username}
                onChange={(e) =>
                  setCreds({ ...creds, username: e.target.value })
                }
              />
              <TextInput
                placeholder="Password"
                icon={faLock}
                type="password"
                value={creds.password}
                onChange={(e) =>
                  setCreds({ ...creds, password: e.target.value })
                }
              />
              <button type="submit" className="btn">
                Sign In
              </button>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};

export default Login;
