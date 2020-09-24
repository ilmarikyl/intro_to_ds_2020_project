import axios from "axios";

export const getUserInfo = async () => {
  const config = {
    headers: {
      Authorization: `bearer AAAAAAAAAAAAAAAAAAAAAFiJHQEAAAAABKimrn2siB%2BSXIJ6s7jwYCgT5pA%3D1PV5oKppu8jR5NTWx26R0dKUHGdWOhTqlwFmaUQmuKxLfA245z`,
    },
  };

  const response = await axios.get(
    `https://cors-anywhere.herokuapp.com/https://api.twitter.com/2/users/by?usernames=realdonaldtrump&user.fields=description,profile_image_url`,
    config
  );
  return response.data;
};
