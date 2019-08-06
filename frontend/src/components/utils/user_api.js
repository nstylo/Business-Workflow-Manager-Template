import axios from 'axios';

// axios headers
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.xsrfCookieName = 'csrftoken';
// postman api key
axios.defaults.headers.common['x-api-key'] =
  process.env.REACT_APP_PSTMN_API_KEY;

/**
 * takes an array of files
 * @param {object} values holds the payload of the request
 */
export async function postFiles(values) {
  const { files, title, description } = values;
  return await axios
    .post('/api/jobs/', {
      files: files || [],
      title: title || '',
      description: description || ''
    })
    .then(response => {
      return response;
    })
    .catch(err => {
      return err.response;
    });
}
