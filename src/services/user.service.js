import axios from 'axios';
import authHeader from './auth-header';
import API_URL from '../constants/apiConstants';

const getPublicContent = (props) => {
    return axios.get(API_URL + props);
};


const getUserBoard = () => {
    return axios.get(API_URL + "/user/", {headers: authHeader() });
};


const getModeratorBoard = () => {
    return axios.get(API_URL + "/auth/user/", { headers: authHeader() });
};


const getAdminBoard = () => {
    return axios.get(API_URL + "/auth/user/", { headers: authHeader() });
};

export default {
    getPublicContent,
    getUserBoard,
    getModeratorBoard,
    getAdminBoard
};

