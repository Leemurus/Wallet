## Задание:
Пишем простой REST сервис (на Django).
Подразумевается, что под ваш REST сервис будет написано отдельное приложение (SPA или мобильное).

#### Сервис по управлению финансами, функционал следующий:
- Пользователь хранит данные о своем "кошельке", произвольное название + баланс в рублях.
- В рамках кошелька ведется история транзакций (как списание, так и пополнение).
- Кошельков может быть больше чем 1, но сам пользователь один (это его персональный веб сервис).

#### API сервиса должен позволять:
- создавать, редактировать и удалять кошелек.
- создавать и удалять транзакции в рамках кошелька (при этом напрямую редактировать баланс кошелька пользователь не может)
транзакции могут быть как +, так и -. то есть транзакции по зачислению денег и списанию.
у каждой транзакции должна быть дата, сумма, произвольный комментарий от пользователя.
- Просматривать список своих кошельков
- Просматривать список своих транзакций как в рамках одного кошелька, так и общий, всех кошельков сразу.

По итогу нужно предоставить исходники сервиса, чтобы мы могли его развернуть (git) и запустить
Для нас интересно: посмотреть на архитектурную организацию кода внутри сервиса, на реализацию тех или иных бизнес требований.

Интересует опыт работы с моделями Django или любого другого, что они могут их собирать в композиции больше чем одна штука и связывать друг с другом.
