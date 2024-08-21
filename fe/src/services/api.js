import Call from "./call";

const Api = () => {
  var setAuthUrl = (path) => {
    return new Call(path);
  };
  var setUrl = (path) => {
    return new Call(`${path}`);
  };

  return {
    server_url: setUrl(),
    ping: setUrl(""),
    signin: setAuthUrl("/users/login"),
    refreshToken: setAuthUrl("/o/token"),
    signOut: setAuthUrl("/dj-rest-auth/logout"),
    passwordReset: setUrl("/users/password_reset"),
    confirmPasswordReset: setUrl("/users/password_reset_confirm"),
    changePassword: setUrl("/users/password_change"),
    register: setUrl("/dj-rest-auth/registration"),
    me: setUrl("/users/me"),
    notifications: setUrl("/notifications/list"),
    clients: setUrl("/notifications/clients"),
    users: setUrl("/users/list"),
  };
};

export default Api();
