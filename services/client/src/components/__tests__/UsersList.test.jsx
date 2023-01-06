import React from 'react';
import { shallow } from 'enzyme';

import UsersList from '../UsersList';

const users = [
  {
    'active': true,
    'email': 'abelthf@gmail.com',
    'id': 1,
    'username': 'fredy'
  },
  {
    'active': true,
    'email': 'fhuancat@unsa.edu.pe',
    'id': 2,
    'username': 'fhuancat'
  }
];

test('UsersList renders properly', () => {
  const wrapper = shallow(<UsersList users={users}/>);
  const element = wrapper.find('h4');
  expect(element.length).toBe(2);
  expect(element.get(0).props.children).toBe('fredy');
});
