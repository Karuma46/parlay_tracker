import axios from "axios";

class Call {
  constructor(endpoint) {
    this.instance = axios.create({
      baseURL: `${this.getApiUrl()}${endpoint}/`,
      // timeout: 30000,
    });
  }

  getApiUrl = () => {
    var url = "http://192.168.45.18:8000";
    if (import.meta.env.VITE_APP_BASE_URL) {
      url = import.meta.env.VITE_APP_BASE_URL;
    }

    return url;
  };

  checkAuth = async () => {
    var token = localStorage.getItem("access_token");
    if (!token) {
      window.location = "/";
    }
  };

  getHeaders = () => {
    var token = localStorage.getItem("access_token");
    if (token) {
      var headers = {
        Authorization: `${token}`,
      };
    } else {
      headers = {};
    }
    return headers;
  };

  get = async (url, params = undefined, signal = undefined) => {
    await this.checkAuth();
    return await this.instance({
      method: "get",
      url: url,
      params: params,
      headers: this.getHeaders(),
      signal: signal,
    });
  };

  post = async (params = undefined) => {
    await this.checkAuth();
    return await this.instance({
      method: "post",
      data: params,
      headers: this.getHeaders(),
    });
  };

  auth = async (params) => {
    return await this.instance({
      method: "post",
      data: params,
      headers: {
        // "Content-Type": "application/x-www-form-urlencoded",
      },
    });
  };

  upload = async (params = undefined) => {
    await this.checkAuth();
    return await this.instance({
      method: "post",
      data: params,
      headers: { ...this.getHeaders(), "Content-Type": undefined },
    });
  };

  put = async (url, params = undefined) => {
    await this.checkAuth();
    return await this.instance({
      method: "put",
      url: url,
      data: params,
      headers: this.getHeaders(),
    });
  };

  patch = async (url, params) => {
    await this.checkAuth();
    return await this.instance({
      method: "patch",
      url: url,
      data: params,
      headers: this.getHeaders(),
    });
  };

  patchupload = async (url, params = undefined) => {
    await this.checkAuth();
    return await this.instance({
      method: "patch",
      url: url,
      data: params,
      headers: { ...this.getHeaders(), "Content-Type": undefined },
    });
  };

  delete = async (url, params = undefined) => {
    await this.checkAuth();
    return await this.instance({
      method: "delete",
      url: url,
      data: params,
      headers: this.getHeaders(),
    });
  };
}

export default Call;
