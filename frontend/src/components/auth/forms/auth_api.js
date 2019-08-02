import axios from 'axios';

// axios headers
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';
// postman api key
axios.defaults.headers.common['x-api-key'] = 'e8f411d2de5d42c485df61bc8a8ff977';

// postman mock api
const test_api_url =
  'https://59a86326-905c-47d9-a33e-383906e3685e.mock.pstmn.io';

/**
 * takes email and password and makes a login request
 */
export async function login(values) {
  const { email, password } = values;
  return await axios
    .post(test_api_url + '/login/', {
      email: email || '',
      password: password || ''
    })
    .then(response => {
      return response;
    })
    .catch(err => {
      return err.response;
    });
}

/**
 * takes user credentials and makes a registration request
 */
export async function register(values) {
  const { email, password, phone, address, company } = values;
  return await axios
    .post(test_api_url + '/register/', {
      email: email || '',
      password: password || '',
      phone: phone || '',
      address: address || '',
      company: company || ''
    })
    .then(response => {
      return response;
    })
    .catch(err => {
      return err.response;
    });
}

/**
 * takes email to request a password reset
 */
export async function requestReset(values) {
  const { email } = values;
  return await axios
    .post(test_api_url + '/request-reset/', {
      email: email || ''
    })
    .then(response => {
      return response;
    })
    .catch(err => {
      return err.response;
    });
}

/**
 * takes password to update the current one
 * TODO: how to identify which password to update?
 */
export async function reset(values) {
  const { password } = values;
  return await axios
    .put(test_api_url + '/reset/', {
      password: password || ''
    })
    .then(response => {
      return response;
    })
    .catch(err => {
      return err.response;
    });
}
