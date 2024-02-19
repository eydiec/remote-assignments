
select article.title, article.author, user.email from assignment.article
inner join assignment.user on user.username= article.author;

select * from assignment.article where 6<id and id<13 
order by id ASC;