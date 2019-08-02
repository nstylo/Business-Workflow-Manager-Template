import auth_const from './auth_const';

/**
 * This interface requires a api request callback and 'instructions'
 * on how to handle those depending on status codes
 * @param {function} callback the api callback on submission
 * @param {object} constants holds status codes and route url on success
 * @param {object} props used for passing on history, so routing is possible
 * @param {object} values the payload of the api call
 * @param {object} bag formik helper functions
 */
export default async function handleSubmit(
  callback,
  constants,
  props,
  values,
  bag
) {
  const { setErrors, setSubmitting } = bag;
  const { status, url } = constants;
  const { history } = props;
  const response = await callback(values);

  switch (response.status) {
    case status.successful:
      history.push(url); // route
      return;
    case status.unsuccessful:
      setErrors(response.data.errors); // errors for the right label
      break;
    default:
      setErrors(auth_const.default_errors.errors); // error on bottom of form
  }

  setSubmitting(false); // do not disable submit button on failure
}