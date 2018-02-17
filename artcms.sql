/*
用户表
0. id编号
1. 账号
2. 密码
3. 注册时间
 */

CREATE TABLE if NOT EXISTS user(
  id int unsigned not null auto_increment key comment "主键ID",
  account varchar(20) not null comment "账号",
  pwd  varchar(100) not null comment "密码",
  addtime datetime not null comment "注册时间"
)engine=InnoDB DEFAULT charset=utf8 comment "用户";

/*
文章表
0. id编号
1. 标题
2. 分类
3. 作者
4. 封面
5. 内容
6. 发布时间
 */
CREATE TABLE if NOT EXISTS article(
  id int unsigned not null auto_increment key comment "主键ID",
  title varchar(100) not null comment "标题",
  category  tinyint unsigned not null comment "分类",
  user_id int unsigned not null comment "作者",
  logo varchar(100) not null comment "封面",
  content mediumtext not null comment "文章",
  addtime datetime not null comment "发表时间"
)engine=InnoDB DEFAULT charset=utf8 comment "文章";